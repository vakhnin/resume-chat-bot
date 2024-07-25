import asyncio
import logging
import sys
from typing import NoReturn

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config.settings import API_TOKEN, db_session
from bot.handlers import unknown, common, images

bot: Bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp: Dispatcher = Dispatcher(bot=bot)


async def shutdown(dispatcher: Dispatcher) -> NoReturn:
    await dispatcher.storage.close()
    await bot.session.close()
    logging.info('Сессия бота закрыта')
    db_session.close()
    logging.info('Сессия BD закрыта')


async def main() -> NoReturn:
    # Registration of handlers
    dp.include_router(common.router)
    dp.include_router(images.router)
    # Registering a handler for an unrecognized command (must be last)
    dp.include_router(unknown.router)

    dp.shutdown.register(shutdown)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit, RuntimeError):
        logging.info('Бот остановлен!')
