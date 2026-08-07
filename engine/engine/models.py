"""
Q-FSI Content Studio
Core Models
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Slide:
    """
    Representa una diapositiva del carrusel.
    """

    number: int

    title: str

    subtitle: str

    body: str

    icon: str = ""

    image: str = ""


@dataclass
class Carousel:

    topic: str

    level: str

    slides: List[Slide] = field(default_factory=list)

    caption: str = ""

    hashtags: List[str] = field(default_factory=list)

    created_at: str = ""

    author: str = "Q-FSI"

    style: str = "Institutional"

    language: str = "es"


@dataclass
class Statistic:

    topic: str

    value: str

    source: str


@dataclass
class Prompt:

    topic: str

    system_prompt: str

    user_prompt: str
