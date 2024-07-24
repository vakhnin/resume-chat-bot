import logging
from pathlib import Path
from typing import Optional

from aiogram import Bot
from aiogram.types import FSInputFile

from bot.config.settings import ADMIN_CHAT_ID


async def get_id(bot: Bot, file: Path) -> Optional[str]:
    if not file.exists():
        return None
    photo: FSInputFile = FSInputFile(file)
    try:
        message = await bot.send_photo(chat_id=ADMIN_CHAT_ID, photo=photo)
    except Exception as e:
        logging.error(e)
        return None

    photo_id: str = message.photo[-1].file_id
    return photo_id
