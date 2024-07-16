from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router: Router = Router()


@router.message(Command('image'))
async def command_image_handler(message: Message) -> None:
    photo_id = 'AgACAgIAAxkDAAOdZpYEvOq-Cv2faST-toG4r4MBoewAAjvrMRvRJLFIqOU1KifnMMQBAAMCAANtAAM1BA'
    await message.answer_photo(photo=photo_id, caption="Here is your image!")
