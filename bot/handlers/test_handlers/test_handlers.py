from pathlib import Path
from typing import NoReturn

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, LinkPreviewOptions

router: Router = Router()


@router.message(Command('test_markup'))
async def test_markup(message: Message) -> NoReturn:
    with open(Path(__file__).parent / "test_markup.txt", "r") as file:
        answer: str = file.read()
        hh_resume_link = LinkPreviewOptions(
            url="https://career.habr.com/svahnin",
            prefer_small_media=True
        )
        await message.answer(
            f"Маленькое превью над текстом\n{answer}",
            link_preview_options=hh_resume_link,
            parse_mode="MarkdownV2"
        )
