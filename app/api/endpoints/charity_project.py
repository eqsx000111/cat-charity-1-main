from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.charity_project import CharityProjectDB, CharityProjectCreate, CharityProjectUpdate
from app.crud.charity_project import charity_project_crud
from app.api.validators import check_project_exists, check_fully_invested
from app.services.investments import invest


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
    project = await charity_project_crud.create(charity_project, session)
    await invest(session=session, new_project=charity_project)
    await session.commit()
    await session.refresh(project)
    return project


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
    project = await check_project_exists(project_id, session)
    await check_fully_invested(project_id, session)
    project = await charity_project_crud.update(project, obj_in, session)
    await session.add(project)
    await session.commit()
    await session.refresh(project)
    return project