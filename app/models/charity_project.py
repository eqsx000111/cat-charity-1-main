from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import AbstractBase


class CharityProject(AbstractBase):
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    def __repr__(self):
        return (
            f'{super().__repr__()}'
            f'name={self.name} '
            f'description={self.description}'
        )
