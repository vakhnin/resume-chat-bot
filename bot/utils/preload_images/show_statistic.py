import logging
import sys
from typing import List, NoReturn

from bot.utils.preload_images.start_preload_images import ProcessedFile, STATUS_PROCESSED, STATUS_ALREADY_IN_DB, \
    STATUS_NOT_GET_ID

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def show_statistic(statistic_list: List[ProcessedFile]) -> NoReturn:
    processed, already_in_db, not_get_id = 0, 0, 0

    item: ProcessedFile
    for item in statistic_list:
        if item.status == STATUS_PROCESSED:
            processed += 1
        elif item.status == STATUS_ALREADY_IN_DB:
            already_in_db += 1
        elif item.status == STATUS_NOT_GET_ID:
            not_get_id += 1
        else:
            logging.error("Неизвестный статус обработки")
    summa: int = processed + already_in_db + not_get_id
    while True:
        print(f"Всего файлов: {summa}")
        print(f"Успешно обработанно: {processed}")
        print(f"Уже в DB: {already_in_db}")
        print(f"Не получен ID: {not_get_id}")
        print(f"Неизвестный статус обработки: {len(statistic_list) - summa}")
        print("\nВыход -  1 \nПросмотр успешно обработанных файлов - 2"
              "\nПросмотр файлов уже в DB - 3 \nПросмотр файлов с неполученным ID - 4")

        try:
            command: int = int(input('Команда [1]: '))
            print()
        except ValueError:
            break
        if command == 1:
            break
        elif command == 2:
            [print(f"{item.catalog}/{item.file}")
             for item in statistic_list if item.status == STATUS_PROCESSED]
        elif command == 3:
            [print(f"{item.catalog}/{item.file}")
             for item in statistic_list if item.status == STATUS_ALREADY_IN_DB]
        elif command == 4:
            [print(f"{item.catalog}/{item.file}")
             for item in statistic_list if item.status == STATUS_NOT_GET_ID]
