import asyncio
import logging
import sys
from asyncio import Task, Lock
from pathlib import Path
from typing import List, NoReturn

from aiogram import Bot

project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))

CATALOGS_LIST: List[Path] = [
    Path('test'),
]

STATUS_PROCESSED: str = 'processed'
STATUS_ALREADY_IN_DB: str = 'already in db'
STATUS_NOT_GET_ID: str = 'not get ID'


class ProcessedFile:
    def __init__(self, catalog: str, file: str, status: str):
        self.catalog: str = catalog
        self.file: str = file
        self.status: str = status

    def __repr__(self) -> str:
        return f"ProcessedFile(catalog={self.catalog!r}, file={self.file!r}, status={self.status!r})"


processed_file_list_lock: Lock = asyncio.Lock()
processed_file_list: List[ProcessedFile] = []


async def main() -> NoReturn:
    from bot.config.settings import PRELOAD_IMAGES_DIR, db_session, API_TOKEN
    from bot.utils.preload_images.show_statistic import show_statistic

    bot: Bot = Bot(token=API_TOKEN)
    tasks: List[Task] = []

    catalog: str
    for catalog in CATALOGS_LIST:
        images_dir: Path = PRELOAD_IMAGES_DIR / catalog

        file: Path
        for file in images_dir.iterdir():
            if file.is_file():
                tasks.append(
                    asyncio.create_task(
                        get_id_save_to_db(bot, file)
                    ))

    await asyncio.gather(*tasks)

    db_session.close()
    logging.info('\nСессия DB закрыта')
    await bot.session.close()
    logging.info('Сессия бота закрыта')

    show_statistic(processed_file_list)


async def get_id_save_to_db(bot: Bot, file: Path) -> NoReturn:
    from bot.utils.preload_images.get_id import get_id
    from bot.config.settings import db_session
    from bot.db.models import Image

    status: str = STATUS_ALREADY_IN_DB
    catalog, file_name = file.parent.name, file.name
    if not db_session.query(Image).filter_by(catalog=catalog, file_name=file_name).count():
        image_id: str = await get_id(bot, file)
        if image_id:
            image = Image(
                catalog=file.parent.name,
                file_name=file.name,
                server_image_id=image_id,
            )
            db_session.add(image)
            db_session.commit()
            status = STATUS_PROCESSED
        else:
            status = STATUS_NOT_GET_ID
    async with processed_file_list_lock:
        processed_file_list.append(ProcessedFile(catalog, file_name, status))
    print(".", end="")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
