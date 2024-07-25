from typing import NoReturn

from aiogram import html, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router: Router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> NoReturn:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(Command('get_chat_id'))
async def get_chat_id_handler(message: Message) -> NoReturn:
    await message.answer('ID этого чата: ' + str(message.chat.id))
