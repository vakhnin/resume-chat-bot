from datetime import datetime

from bot.config.settings import db_session, IMAGES_DIR
from bot.db.models import Image

path = IMAGES_DIR / 'test_images' / 'telegram-dark.png'
print(path.stat().st_ctime)
file_creation_date = datetime.fromtimestamp(path.stat().st_ctime)

image = Image(
    catalog='test_images',
    file_name='telegram-dark.png',
    file_date=file_creation_date,
    server_image_id='id',
    server_image_id_date=datetime.now(),
)
db_session.add(image)
db_session.commit()
print(db_session.query(Image).all())
