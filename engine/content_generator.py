"""
==========================================================
Q-FSI Content Studio
Content Generator Engine
Versión 1.0
==========================================================
"""

from dataclasses import dataclass, asdict
from typing import List, Dict
import random

# ----------------------------------------------------------
# Hooks
# ----------------------------------------------------------

HOOKS = [
    "El 90% de las personas comete este error financiero.",
    "Si entiendes esto, tu relación con el dinero cambiará.",
    "Nadie te enseñó esto en la escuela.",
    "Antes de invertir, debes saber esto.",
    "Este hábito puede cambiar tus finanzas."
]

# ----------------------------------------------------------
# CTA
# ----------------------------------------------------------

CTA = [
    "Guarda este carrusel para leerlo más tarde.",
    "Compártelo con alguien que lo necesite.",
    "Sígueme para aprender sobre inversión y finanzas.",
    "¿Qué opinas? Escríbelo en los comentarios."
]

# ----------------------------------------------------------
# Hashtags base
# ----------------------------------------------------------

BASE_HASHTAGS = [
    "#Finanzas",
    "#EducacionFinanciera",
    "#Inversion",
    "#Dinero",
    "#LibertadFinanciera",
    "#ETF",
    "#Bolsa",
    "#Ahorro"
]

# ----------------------------------------------------------
# Estadísticas (ejemplos)
# ----------------------------------------------------------

STATS = {
    "Mentalidad financiera":
        "Las personas que establecen metas financieras por escrito tienen más probabilidades de seguir un plan financiero.",

    "Interés compuesto":
        "Comenzar a invertir antes suele tener más impacto que intentar aportar grandes cantidades más adelante.",

    "Cómo ahorrar":
        "Automatizar el ahorro puede facilitar mantener el hábito de forma constante."
}

# ----------------------------------------------------------
# Estructuras
# ----------------------------------------------------------

@dataclass
class Slide:

    title: str
    subtitle: str
    body: str
    icon: str

@dataclass
class Carousel:

    slide1: Slide
    slide2: Slide
    slide3: Slide
    slide4: Slide
    slide5: Slide

    caption: str
    hashtags: List[str]

# ----------------------------------------------------------
# Generador
# ----------------------------------------------------------

class ContentGenerator:

    def __init__(self):

        pass

    def create(self, topic: str) -> Dict:

        hook = random.choice(HOOKS)

        stat = STATS.get(
            topic,
            "La educación financiera ayuda a tomar decisiones más informadas."
        )

        slide1 = Slide(
            title=topic,
            subtitle=hook,
            body="Desliza para descubrir cómo aplicar este concepto en tu vida financiera.",
            icon="📈"
        )

        slide2 = Slide(
            title="¿Qué significa?",
            subtitle="Concepto",
            body=f"{topic} explicado de forma sencilla para cualquier persona.",
            icon="📚"
        )

        slide3 = Slide(
            title="Ejemplo práctico",
            subtitle="Caso real",
            body=(
                "Si una persona ahorra $200 al mes y obtiene un rendimiento anual, "
                "el crecimiento del capital dependerá del tiempo, las aportaciones y la rentabilidad."
            ),
            icon="💰"
        )

        slide4 = Slide(
            title="Errores comunes",
            subtitle="Evítalos",
            body=(
                "• Actuar por emociones.\n"
                "• No tener un plan.\n"
                "• Buscar ganancias rápidas.\n"
                "• No diversificar."
            ),
            icon="⚠️"
        )

        slide5 = Slide(
            title="Conclusión",
            subtitle="Empieza hoy",
            body=random.choice(CTA),
            icon="🚀"
        )

        caption = f"""
{hook}

Hoy hablamos sobre **{topic}**.

Dato clave:

{stat}

¿Qué hábito financiero estás construyendo este año?

👇 Te leo en los comentarios.
"""

        hashtags = BASE_HASHTAGS + [
            "#" + topic.replace(" ", "")
        ]

        carousel = Carousel(
            slide1,
            slide2,
            slide3,
            slide4,
            slide5,
            caption.strip(),
            hashtags
        )

        return asdict(carousel)
