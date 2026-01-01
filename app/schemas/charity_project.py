from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, PositiveInt


class CharityProjectBase(BaseModel):
    name: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=10)


class CharityProjectCreate(CharityProjectBase):
    full_amount: PositiveInt


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: datetime | None

    model_config = ConfigDict(from_attributes=True)


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str] = Field(min_length=5, max_length=100)
    description: Optional[str] = Field(min_length=10)
