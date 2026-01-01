from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation
from app.crud.charity_project import charity_project_crud
# from app.crud.donation import r


async def check_project_exists(
        meeting_room_id: int,
        session: AsyncSession
) -> CharityProject:
    project = await charity_project_crud.get(meeting_room_id, session)
    if project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return project