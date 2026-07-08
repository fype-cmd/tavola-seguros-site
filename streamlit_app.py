"""
Távola Corretora de Seguros — wrapper Streamlit para publicar a landing page.

Como rodar localmente:
    pip install -r requirements.txt
    streamlit run streamlit_app.py

Como publicar (Streamlit Community Cloud):
    1. Suba esta pasta para um repositório no GitHub.
    2. Em https://share.streamlit.io conecte o repo e aponte para streamlit_app.py.
    3. Pronto — o site fica no ar em um link .streamlit.app

A página HTML é renderizada em tela cheia, sem a barra/menu padrão do Streamlit.
"""
from pathlib import Path
import base64
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Távola Corretora de Seguros",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Esconde o "enfeite" padrão do Streamlit e faz o iframe ocupar a tela inteira
st.markdown(
    """
    <style>
      #MainMenu, header[data-testid="stHeader"], footer, .stDeployButton { display: none !important; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      .stApp { background: #f7f3ea; }
      /* iframe do componente HTML ocupa toda a altura da janela */
      iframe { height: 100vh !important; width: 100% !important; border: none !important; }
      div[data-testid="stAppViewBlockContainer"] { padding: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE = Path(__file__).parent
html = (BASE / "index.html").read_text(encoding="utf-8")

# Embute a foto do hero (assets/hero.jpg) como base64, se existir,
# para que ela funcione dentro do iframe do Streamlit.
hero = BASE / "assets" / "hero.jpg"
if hero.exists():
    b64 = base64.b64encode(hero.read_bytes()).decode()
    html = html.replace('src="assets/hero.jpg"', f'src="data:image/jpeg;base64,{b64}"')

# scrolling=True permite rolar a página inteira dentro do iframe (que ocupa 100vh)
components.html(html, height=1000, scrolling=True)
