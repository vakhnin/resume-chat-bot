from pathlib import Path
from typing import NoReturn

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router: Router = Router()


@router.message(Command('test_markup'))
async def test_markup(message: Message) -> NoReturn:
    with open(Path(__file__).parent / "test_markup.txt", "r") as file:
        answer: str = file.read()
        await message.answer(answer, parse_mode="MarkdownV2")
