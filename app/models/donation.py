from sqlalchemy import Text
from sqlalchemy.orm import mapped_column, Mapped

from app.core.db import AbstractBase


class Donation(AbstractBase):
    comment: Mapped[str] = mapped_column(Text, nullable=True)
