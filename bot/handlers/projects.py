from typing import Optional, NoReturn

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config.settings import db_session
from bot.db.models import Project, ProjectsList

router: Router = Router()


@router.message(Command('project'))
async def command_image_handler(message: Message) -> NoReturn:
    project: Optional[Project] = db_session.query(Project).first()
    if project:
        await message.answer(project.description)


@router.message(Command('projects'))
async def command_image_handler(message: Message) -> NoReturn:
    project_list: Optional[ProjectsList] = db_session.query(ProjectsList).first()
    answer: str = ""
    if project_list:
        for item in project_list.projects:
            answer += item.projects.shot_description + "\n"
        await message.answer(answer)
