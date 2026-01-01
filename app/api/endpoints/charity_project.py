from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.charity_project import CharityProjectDB, CharityProjectCreate, CharityProjectUpdate
from app.crud.charity_project import charity_project_crud


router = APIRouter()
SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@router.get(
        '/',
        response_model=list[CharityProjectDB],
        response_model_exclude_none=True
)
async def get_all_charity_project(session: SessionDep):
    return await charity_project_crud.get_multi(session)


@router.post(
        '/',
        response_model=CharityProjectDB,
        response_model_exclude_none=True
)
async def create_new_charity_project(
    charity_project: CharityProjectCreate,
    session: SessionDep
):
    return await charity_project_crud.create(charity_project, session)


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True
)
async def update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: SessionDep
):
    