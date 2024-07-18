from typing import List

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InputMediaPhoto

router: Router = Router()


@router.message(Command('image'))
async def command_image_handler(message: Message) -> None:
    photo_id = 'AgACAgIAAxkDAAMWZpja1TxGD4UvdbRtZszWBCHY66sAAiXaMRssQ8hIPqJjpLWs9zABAAMCAANtAAM1BA'
    await message.answer_photo(photo=photo_id, caption="Here is your image!")


@router.message(Command('images'))
async def command_image_handler(message: Message) -> None:
    media_group: List[InputMediaPhoto] = [
        InputMediaPhoto(media='AgACAgIAAxkDAAMVZpja1JtgJE4EuYeBeo9rrS6DN0gAAiTaMRssQ8hIfpFqBFH3lrUBAAMCAANtAAM1BA'),
        InputMediaPhoto(media='AgACAgIAAxkDAAMWZpja1TxGD4UvdbRtZszWBCHY66sAAiXaMRssQ8hIPqJjpLWs9zABAAMCAANtAAM1BA')
    ]
    await message.answer_media_group(media=media_group, caption="Here is your image!")
