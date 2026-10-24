import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
rng=np.random.default_rng(7)
OUT='fotos/'

def tone(L, warm=1.0):
    L=np.clip(L,0,1)
    stops=np.array([0,.35,.7,1.0])
    cols=np.array([[11,20,36],[52,66,90],[150,154,160],[240,234,222]],float)
    out=np.stack([np.interp(L,stops,cols[:,c]) for c in range(3)],-1)
    return out

def finish(L,name,grain=.025,vig=.55,q=82):
    h,w=L.shape
    y,x=np.mgrid[0:h,0:w]
    d=np.sqrt(((x-w/2)/(w/2))**2+((y-h/2)/(h/2))**2)
    L=L*(1-vig*np.clip(d-.35,0,1)**1.6)
    rgb=tone(L)
    rgb+=rng.normal(0,255*grain,rgb.shape)
    Image.fromarray(np.clip(rgb,0,255).astype(np.uint8)).save(OUT+name,quality=q,optimize=True,progressive=True)

def shelves(w,h,shelf=190,seed=1,base=.18):
    r=np.random.default_rng(seed)
    L=np.full((h,w),base)
    for top in range(-r.integers(0,shelf),h,shelf):
        board=top+shelf-18
        x=0
        while x<w:
            bw=int(r.integers(12,38)); bh=int(r.integers(int(shelf*.55),shelf-28))
            if r.random()<.06: x+=int(r.integers(20,70)); continue
            lum=r.uniform(.12,.6)
            if r.random()<.15: lum=r.uniform(.6,.8)
            y0=max(board-bh,0); 
            if board>0: L[y0:max(board,0),x:x+bw]=lum
            # band on spine
            if r.random()<.5 and board-bh+20<board: L[max(board-bh+18,0):max(board-bh+24,0),x:x+bw]=lum*1.25
            x+=bw+int(r.integers(1,4))
        if 0<board<h: L[board:min(board+18,h),:]=.32
        if 0<board+18<h: L[board+18:min(board+24,h),:]=.08
    return L

def light(w,h,cx,cy,rad,amp):
    y,x=np.mgrid[0:h,0:w]
    return amp*np.exp(-(((x-cx)/rad)**2+((y-cy)/(rad*1.3))**2))

# A: biblioteca (hero)
w,h=1920,1100
L=shelves(w,h,200,seed=3)
L=gaussian_filter(L,7)
L=L*(.55+light(w,h,-200,350,1300,.9))+light(w,h,-100,300,700,.35)
for _ in range(9):  # bokeh
    cx,cy,rr=rng.uniform(1100,1900),rng.uniform(100,700),rng.uniform(25,60)
    yy,xx=np.mgrid[0:h,0:w]; L+=.10*((xx-cx)**2+(yy-cy)**2<rr**2)
L=gaussian_filter(L,2)
# mesa em primeiro plano
yy=np.arange(h)[:,None]
desk=(yy>930)
L=np.where(desk,.07+ .05*np.exp(-((yy-940)/6.0)**2),L)
L+=.22*np.exp(-((yy-932)/3.0)**2)*np.linspace(1,.2,w)[None,:]
finish(L,'escritorio-biblioteca.jpg')

# B: sala de reunião
w,h=1600,1000
L=np.full((h,w),.2)
y,x=np.mgrid[0:h,0:w]
for i,x0 in enumerate(range(120,1500,260)):   # janelas
    L[80:560,x0:x0+220]=.86
    L[80:560,x0+105:x0+115]=.35
for yb in range(90,560,22): L[yb:yb+3,100:1500]*=.82   # persianas
L[560:600,:]=.3
L=gaussian_filter(L,5)
# mesa em perspectiva
top=np.interp(x,[0,w],[640,640]); 
tbl=(y>640+0*(x))&(np.abs(x-w/2)< (y-560)*2.4)
L=np.where(tbl,.16+.25*np.exp(-((x-w*.42)/260)**2)*np.exp(-((y-700)/90)**2),L)
L+=.25*np.exp(-((y-642)/3)**2)*(np.abs(x-w/2)<220)
# cadeiras
for cx in [w/2-460,w/2-250,w/2+250,w/2+460]:
    m=((x-cx)/70)**2+((y-660)/120)**4<1
    L=np.where(m,.06,L)
for cx in [w/2-620,w/2+620]:
    m=((x-cx)/95)**2+((y-760)/170)**4<1
    L=np.where(m,.05,L)
L=gaussian_filter(L,4.5)
L=L*(.7+light(w,h,w*.4,300,900,.45))
finish(L,'escritorio-reuniao.jpg')

# C: estudo (retrato) - estante com luminária
w,h=1200,1500
L=shelves(w,h,230,seed=11,base=.14)
L=gaussian_filter(L,9)*(.5+light(w,h,1300,200,1100,.8))
L+=light(w,h,880,420,120,.55)+light(w,h,880,420,260,.2)
y,x=np.mgrid[0:h,0:w]
L=np.where(y>1150,.09,L); L+=.3*np.exp(-((y-1152)/3)**2)*np.linspace(.2,1,w)[None,:]
# pilha de documentos
for i in range(5):
    y0=1150-14*(i+1); m=(y>y0)&(y<y0+11)&(x>260+i*6)&(x<760-i*4)
    L=np.where(m,.72-.05*i,L)
L=gaussian_filter(L,1.2)
finish(L,'escritorio-estudo.jpg')

# D: retratos (silhueta contra estante desfocada)
def retrato(name,seed,lx):
    w,h=1000,1250
    L=gaussian_filter(shelves(w,h,210,seed=seed,base=.2),14)*(.6+light(w,h,lx,300,900,.7))
    y,x=np.mgrid[0:h,0:w]
    head=((x-500)/135)**2+((y-470)/175)**2<1
    neck=(np.abs(x-500)<62)&(y>580)&(y<680)
    sh=(y>660)&(np.abs(x-500)< 200+ (y-660)*1.6)
    sh=sh&(((x-500)/470)**2+((y-1250)/600)**2<1.05)
    body=head|neck|sh
    L=np.where(body,.09,L)
    shirt=(y>650)&(np.abs(x-500)< (y-650)*0.28)&(y<900)
    L=np.where(shirt,.62,L)
    tie=(y>670)&(np.abs(x-500)< 10+(y-670)*0.05)&(y<1050)&sh
    L=np.where(tie,.16,L)
    L=gaussian_filter(L,7)
    # rim light
    edge=gaussian_filter(body.astype(float),6)-gaussian_filter(body.astype(float),2)
    side=np.clip((lx-x)/w*-1+.5,0,1) if lx>500 else np.clip((500-x)/500,0,1)
    L+=np.clip(-edge,0,1)*.0+np.clip(edge,0,1)*0
    L+=0.35*np.clip(gaussian_filter(body.astype(float),3)-body,0,1)*0
    finish(L,name,vig=.45)
retrato('equipe-1.jpg',21,-100)
retrato('equipe-2.jpg',33,1100)
retrato('equipe-3.jpg',45,-100)
