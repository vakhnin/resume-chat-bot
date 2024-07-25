from typing import List, Optional, NoReturn, Type

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InputMediaPhoto

from bot.config.settings import db_session
from bot.db.models import Image

router: Router = Router()


@router.message(Command('image'))
async def command_image_handler(message: Message) -> NoReturn:
    image: Optional[Image] = db_session.query(Image).first()
    if image:
        await message.answer_photo(photo=image.server_image_id, caption="Here is your image!")


@router.message(Command('images'))
async def command_image_handler(message: Message) -> NoReturn:
    command_parts: List[str] = message.text.split(maxsplit=1)
    if len(command_parts) < 2:
        return
    catalog: str=command_parts[1]
    images: List[Type[Image]] = db_session.query(Image).filter(Image.catalog == catalog).all()
    if images:
        media_group: List[InputMediaPhoto] = []
        for image in images:
            media_group.append(InputMediaPhoto(media=image.server_image_id, caption=image.file_name))
        await message.answer_media_group(media=media_group, caption="Here is your images!")
