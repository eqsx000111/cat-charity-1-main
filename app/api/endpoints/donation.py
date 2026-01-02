from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session

router = APIRouter()
SessionDep = Annotated[AsyncSession, Depends(get_async_session)]