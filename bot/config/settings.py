import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session

from bot.db.models import Base

BASE_DIR: Path = Path(__file__).parent.parent.parent
DATA_DIR: Path = BASE_DIR / 'bot' / 'data'
PRELOAD_IMAGES_DIR: Path = DATA_DIR / 'preload_img'
DATABASE_URL: str = f'sqlite:///{BASE_DIR / "bot.sqlite"}'

load_dotenv(BASE_DIR / '.env')

API_TOKEN: str = os.environ.get('ENV_API_TOKEN')
ADMIN_CHAT_ID: str = os.environ.get('ENV_ADMIN_CHAT_ID')

if not API_TOKEN:
    print('Значение переменной окружения ENV_TOKEN не задано')
    exit(-1)
if not ADMIN_CHAT_ID:
    print('Значение переменной окружения ADMIN_CHAT_ID не задано')
    exit(-1)

# db_engine: Engine = create_engine(DATABASE_URL, echo=True)
db_engine: Engine = create_engine(DATABASE_URL)
db_session: Session = Session(bind=db_engine)
Base.metadata.create_all(bind=db_engine)
