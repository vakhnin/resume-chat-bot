from pathlib import Path
from typing import Union, Optional

from aiogram import Bot
from aiogram.types import FSInputFile, Message


async def upload_image(bot: Bot, file_path: Path) -> Optional[str]:
    if not file_path.exists():
        return None
    photo: FSInputFile = FSInputFile(file_path)
    message = await bot.send_photo(chat_id=111111111, photo=photo)

    photo_id: str = message.photo[-1].file_id
    return photo_id
