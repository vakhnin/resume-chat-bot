import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR: Path = Path(__file__).parent.parent.parent
IMAGES_DIR: Path = BASE_DIR / 'bot' / 'data' / 'img'

load_dotenv(BASE_DIR / '.env')

API_TOKEN: str = os.environ.get('ENV_API_TOKEN')
ADMIN_CHAT_ID: str = os.environ.get('ENV_ADMIN_CHAT_ID')

if not API_TOKEN:
    print('Значение переменной окружения ENV_TOKEN не задано')
    exit(-1)
if not ADMIN_CHAT_ID:
    print('Значение переменной окружения ADMIN_CHAT_ID не задано')
    exit(-1)
