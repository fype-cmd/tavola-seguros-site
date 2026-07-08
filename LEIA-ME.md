# Távola Corretora de Seguros — Landing Page

Landing page de página única (verde + dourado), pronta para publicar.

## Arquivos
- `index.html` — o site inteiro (HTML + CSS + JS num arquivo só). Abra no navegador para ver.
- `streamlit_app.py` — wrapper para publicar no Streamlit.
- `requirements.txt` — dependência (streamlit).
- `assets/` — coloque aqui `hero.jpg` (foto da família) e, se quiser, `logo.png`.

## Ver no navegador (sem instalar nada)
Dê dois cliques em `index.html`.

## Publicar no Streamlit Cloud
1. Suba esta pasta para um repositório no GitHub.
2. Acesse https://share.streamlit.io, conecte o repo e aponte para `streamlit_app.py`.
3. O site fica no ar em um link `.streamlit.app`.

Para testar local: `pip install -r requirements.txt` e depois `streamlit run streamlit_app.py`.

## O que EDITAR (procure "EDITAR AQUI" no index.html)
- **WhatsApp**: troque `5531999999999` pelo número real (55 + DDD + número).
- **Foto do hero**: salve a imagem da família em `assets/hero.jpg`.
- **Números da seção de estatísticas** (anos, clientes, seguradoras, satisfação).
- **Logos dos parceiros** (hoje são nomes; troque por `<img src="assets/porto.png">`).
- **Depoimentos** (nomes e textos reais dos clientes).
- **Contato**: telefone, e-mail, localização e horários no rodapé.
