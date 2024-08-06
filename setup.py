import json
import logging
import sys
from pathlib import Path
from typing import Tuple, NoReturn, Dict

from sqlalchemy.exc import IntegrityError

from bot.config.settings import db_session, DATA_DIR
from bot.db.models import Page, Project

CATALOGS_LIST: Dict = {
    "pages": Page,
    "projects": Project,
}


def main() -> NoReturn:
    catalog: str
    for catalog, data_class in CATALOGS_LIST.items():
        data_dir: Path = DATA_DIR / catalog

        file_path: Path
        for file_path in data_dir.iterdir():
            catalog, file_name = str(file_path.parent.name), str(file_path.name)
            if file_path.is_file():
                if db_session.query(data_class).filter_by(catalog=catalog, source_file=file_name).count():
                    continue
                try:
                    with open(file_path, "r", encoding="UTF-8") as file:
                        data = json.load(file)
                    project = data_class(**data)
                    project.catalog = catalog
                    project.source_file = file_name
                    db_session.add(project)
                    db_session.commit()
                except json.JSONDecodeError as e:
                    logging.error(f"Ошибка разбора JSON в файле {catalog}/{file_name}: {e}")
                except IntegrityError as e:
                    if 'NOT NULL constraint failed' in str(e.orig):
                        logging.error(f"В файле {catalog}/{file_name} заполнены не все необходимые поля")
                    else:
                        logging.error(f"Неизвестная ошибка IntegrityError в файле {catalog}/{file_name}: {e.orig}")
                    db_session.rollback()
                except Exception as e:
                    db_session.rollback()
                    print(f"Error: {e}")

    db_session.close()
    logging.info('\nСессия DB закрыта')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
