import asyncio

from aiogram import Bot

from bot.config.settings import IMAGES_DIR, API_TOKEN
from bot.services.image_service import upload_image

bot = Bot(token=API_TOKEN)


async def main():
    image_paths = [
        IMAGES_DIR / 'test_images' / 'telegram-dark.png',
        IMAGES_DIR / 'test_images' / 'telegram-light.png',
    ]
    image_ids = []

    for image_path in image_paths:
        image_id = await upload_image(bot, image_path)
        if image_id:
            image_ids.append(image_id)
            print(f'Uploaded {image_path}, got file_id: {image_id}')
        else:
            print(f'{image_path} not exists')

    with open('image_ids.txt', 'w') as f:
        for image_id in image_ids:
            f.write(image_id + '\n')

    await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
