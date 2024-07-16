from aiogram import Bot
from aiogram.types import FSInputFile

from bot.config.settings import API_TOKEN



async def upload_image(bot ,file_path: str) -> str:
    with open(file_path, 'rb') as file:
        photo = FSInputFile(file_path)
        message = await bot.send_photo(chat_id=111111111, photo=photo)

        photo_id = message.photo[-1].file_id
        return photo_id
