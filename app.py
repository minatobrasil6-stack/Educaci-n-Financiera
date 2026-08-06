import json
from pathlib import Path

import streamlit as st

from config import (
    BRAND_NAME,
    BRAND_SUBTITLE,
    CONTENT_DIR,
    COLORS,
)

# -----------------------------
# Configuración de la página
# -----------------------------

st.set_page_config(
    page_title=f"{BRAND_NAME} Content Studio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CSS
# -----------------------------

st.markdown(f"""
<style>

html, body, [class*="css"] {{
    background-color:{COLORS["background"]};
    color:white;
}}

.main {{
    background-color:{COLORS["background"]};
}}

.block-container {{
    padding-top:2rem;
    padding-bottom:2rem;
}}

.qfsi-card {{
    background:{COLORS["panel"]};
    border:1px solid #2a2a2a;
    border-radius:14px;
    padding:20px;
}}

.big-title{{
    font-size:42px;
    font-weight:800;
}}

.gold{{
    color:{COLORS["gold"]};
}}

.slide-preview{{
    border:1px solid #2c2c2c;
    border-radius:12px;
    height:260px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:22px;
    background:#111;
}}

div.stButton > button {{
    width:100%;
    height:52px;
    font-size:18px;
    font-weight:bold;
    border-radius:12px;
}}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Leer temas
# -----------------------------

topics_file = CONTENT_DIR / "topics.json"

if topics_file.exists():

    with open(topics_file, "r", encoding="utf-8") as f:

        topics = json.load(f)

else:

    topics = [
        "Mentalidad financiera",
        "Cómo ahorrar",
        "Interés compuesto",
        "ETF",
        "Bolsa",
    ]

# -----------------------------
# Header
# -----------------------------

st.markdown(f"""
<div class='big-title'>
{BRAND_NAME}
<span class='gold'>Content Studio</span>
</div>

{BRAND_SUBTITLE}
""", unsafe_allow_html=True)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("⚙ Configuración")

    tema = st.selectbox(
        "Tema",
        topics
    )

    nivel = st.selectbox(
        "Nivel",
        [
            "Principiante",
            "Intermedio",
            "Avanzado"
        ]
    )

    objetivo = st.selectbox(
        "Objetivo",
        [
            "Educar",
            "Viralizar",
            "Vender",
            "Autoridad"
        ]
    )

    estilo = st.selectbox(
        "Estilo",
        [
            "Bloomberg",
            "BlackRock",
            "Goldman Sachs",
            "Minimalista"
        ]
    )

    marca = st.text_input(
        "Nombre de marca",
        BRAND_NAME
    )

    generar = st.button(
        "🚀 Generar Carrusel"
    )

# -----------------------------
# Layout
# -----------------------------

col1, col2 = st.columns([1, 1])

# -----------------------------
# Panel izquierdo
# -----------------------------

with col1:

    st.subheader("Información")

    st.markdown(f"""
**Tema**

{tema}

**Nivel**

{nivel}

**Objetivo**

{objetivo}

**Estilo**

{estilo}
""")

# -----------------------------
# Panel derecho
# -----------------------------

with col2:

    st.subheader("Vista previa")

    for i
