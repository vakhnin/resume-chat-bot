import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import unknown, common

TOKEN = os.environ.get('ENV_TOKEN')

if not TOKEN:
    print('Значение переменной окружения ENV_TOKEN не задано')
    exit(-1)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(bot=bot)

    # Registration of handlers
    dp.include_router(common.router)
    # Registering a handler for an unrecognized command (must be last)
    dp.include_router(unknown.router)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
