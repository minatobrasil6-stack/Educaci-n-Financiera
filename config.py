"""
===========================================
Q-FSI Content Studio
Global Configuration
===========================================
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# --------------------------------------------------
# Cargar variables de entorno
# --------------------------------------------------

load_dotenv()

# --------------------------------------------------
# Directorios
# --------------------------------------------------

BASE_DIR = Path(__file__).parent

ASSETS_DIR = BASE_DIR / "assets"
TEMPLATES_DIR = BASE_DIR / "templates"
CONTENT_DIR = BASE_DIR / "content"
ENGINE_DIR = BASE_DIR / "engine"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# --------------------------------------------------
# Marca
# --------------------------------------------------

BRAND_NAME = "Q-FSI"

BRAND_SUBTITLE = "Institutional Financial Intelligence"

LOGO_PATH = ASSETS_DIR / "logo.png"

# --------------------------------------------------
# Instagram
# --------------------------------------------------

INSTAGRAM = {
    "width": 1080,
    "height": 1350,
    "dpi": 300
}

# --------------------------------------------------
# Paleta institucional
# --------------------------------------------------

COLORS = {

    "background": "#0B0F19",

    "panel": "#141B22",

    "gold": "#C8A23A",

    "white": "#FFFFFF",

    "text": "#EAEAEA",

    "gray": "#B0B5BE",

    "green": "#18B875",

    "red": "#D9534F",

    "blue": "#4E89FF"

}

# --------------------------------------------------
# Tipografías
# --------------------------------------------------

FONTS = {

    "title": "Fraunces",

    "subtitle": "Inter",

    "body": "Inter",

    "numbers": "JetBrains Mono"

}

# --------------------------------------------------
# Iconografía
# --------------------------------------------------

ICONS = {

    "money": "💰",

    "chart": "📈",

    "warning": "⚠",

    "idea": "💡",

    "book": "📚",

    "rocket": "🚀"

}

# --------------------------------------------------
# Exportación
# --------------------------------------------------

EXPORT = {

    "png": True,

    "pdf": False,

    "zip": True

}

# --------------------------------------------------
# OpenAI
# --------------------------------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# --------------------------------------------------
# Supabase
# --------------------------------------------------

SUPABASE_URL = os.getenv("SUPABASE_URL", "")

SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# --------------------------------------------------
# Temas
# --------------------------------------------------

DEFAULT_LEVEL = "Principiante"

DEFAULT_STYLE = "Institutional"

DEFAULT_LANGUAGE = "es"

# --------------------------------------------------
# Carrusel
# --------------------------------------------------

SLIDES_PER_CAROUSEL = 5

MAX_TITLE = 60

MAX_SUBTITLE = 120

MAX_BODY = 700

# --------------------------------------------------
# Exportación
# --------------------------------------------------

IMAGE_FORMAT = "PNG"

IMAGE_QUALITY = 95

# --------------------------------------------------
# Footer
# --------------------------------------------------

FO
