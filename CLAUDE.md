# Site — Batista & Rocha Advogados Associados

> Contexto completo de negócio, público-alvo, posicionamento, tom de voz e regras éticas: leia o `README.md` antes de escrever ou alterar qualquer texto.

Site institucional do escritório (Brasília-DF, atuação nacional). HTML, CSS e JS puros, num único `index.html`, sem build. Navegação por âncora (`#inicio`, `#penal-economico`...), cada página é um `<div data-page="...">`.

## Estrutura
- `index.html` — todas as páginas, estilos e script.
- `fotos/` — imagens ILUSTRATIVAS (geradas). Substituir pelas reais mantendo os nomes de arquivo.
- `assets/logo/` — logo completa e monograma em SVG (cor #162947). No HTML eles estão embutidos como `<symbol id="logo">` e `<symbol id="mono">` com `fill="currentColor"`.
- `ferramentas/gerar-fotos-ilustrativas.py` — script que gerou as fotos provisórias (Python, numpy, scipy, Pillow).

## Identidade visual (não alterar sem aprovação)
- Cores: azul da marca #162947 · azul profundo #0E1B30 · azul névoa #B9C3D1 · prata #D9DADC · gelo #F5F5F3 · grafite #2B2F36 · cinza texto #5E6E85. Sem dourado.
- Fontes: Cormorant Garamond (títulos) e Montserrat (texto, rótulos).
- Alinhamento à esquerda, cantos retos, fio de 120 px como ornamento. Logo só em azul ou branco, sem sombra nem degradê. Nunca usar símbolo da OAB.

## Regras éticas (Provimento 205/2021 da OAB) — valem para todo texto do site
- O site informa, não vende. Nada de "contrate", "fale conosco agora", "ligue já".
- Proibido: caso concreto (mesmo anonimizado), cliente, resultado, promessa ou sugestão de resultado, valores/honorários/"consulta gratuita", superlativos e comparações ("melhor", "referência", "número 1"), ostentação, depoimentos.
- Nenhum advogado do escritório tem título de especialização: NUNCA usar "especialista", "especializado(a)", "especialização", "pós-graduado" ou "notória especialização". Usar "advogado criminalista", "atua em".
- "Atendimento 24 horas" pode aparecer no site (publicidade passiva), sem tom de urgência, sem sirene, sem "plantão".
- Imagens proibidas: algemas, viaturas, celas, violência, balança/martelo, dinheiro, carros, luxo, vista ou tamanho do escritório em destaque.
- Toda identificação profissional leva nome + OAB.
- Toda citação de lei/artigo precisa ser verificada; na dúvida, marcar [VERIFICAR].

## Equipe
- Gustavo Batista — OAB/DF 60.823 — Sócio. Advogado criminalista há mais de oito anos; defesa criminal e TCU.
- Lucas Rocha Freitas — OAB/DF 74.242 · OAB/SP 505.896 — Sócio. Processos penais envolvendo crimes econômicos e contencioso empresarial (penal, trabalhista, cível).
- [Nome a confirmar] — OAB/DF 79.624 — Advogada (cível e trabalhista). Nunca chamar de "sócia".

## Pendências (spans com classe `.pend`)
Nome da advogada · telefone/WhatsApp · endereço · horário presencial · nº de registro da sociedade na OAB/DF · CNPJ · ano de fundação e história · formação dos advogados · fotos reais · política de cookies.
Antes de publicar: remover a barra "Protótipo" (`.proto`) e fazer o botão WhatsApp (`.wpp`) apontar para `https://wa.me/55DDDNUMERO`.

## Aprovação
Nenhuma alteração de texto vai ao ar sem ok por escrito do Lucas e do Gustavo.
