from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation


async def invest(
        session: AsyncSession
):
    projects = await session.execute(
        select(CharityProject)
        .where(CharityProject.fully_invested.is_(False))
        .order_by(CharityProject.create_date)
    )
    projects = projects.scalars().all()
    donations = await session.execute(
        select(Donation)
        .where(Donation.fully_invested.is_(False))
        .order_by(Donation.create_date)
    )
    donations = donations.scalars().all()

    project_index = 0
    donation_index = 0
    while project_index < len(projects) and donation_index < len(donations):
        project = projects[project_index]
        donation = donations[donation_index]
        project_need = project.full_amount - project.invested_amount
        donation_free = donation.full_amount - donation.invested_amount
        invested_amount = min(project_need, donation_free)
        project.invested_amount += invested_amount
        donation.invested_amount += invested_amount
        if project.invested_amount >= project.full_amount:
            project.fully_invested = True
            project.close_date = datetime.now()
            project_index += 1
        if donation.invested_amount >= donation.full_amount:
            donation.fully_invested = True
            donation.close_date = datetime.now()
            donation_index += 1

        session.add(project)
        session.add(donation)


def recalculate_project_state(project: CharityProject) -> None:
    if project.invested_amount >= project.full_amount:
        project.fully_invested = True
        project.close_date = datetime.now()
