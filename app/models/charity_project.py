from sqlalchemy import String, Text
from sqlalchemy.orm import mapped_column, Mapped

from app.core.db import AbstractBase


class CharityProject(AbstractBase):
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
