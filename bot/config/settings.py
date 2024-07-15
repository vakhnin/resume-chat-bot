import os
from pathlib import Path

BOT_ROOT_DIR = Path(__file__).parent.parent
IMAGES_DIR = BOT_ROOT_DIR / 'data' / 'img'

API_TOKEN = os.environ.get('ENV_API_TOKEN')

if not API_TOKEN:
    print('Значение переменной окружения ENV_TOKEN не задано')
    exit(-1)
