from aiogram.types import FSInputFile


async def upload_image(bot, file_path) -> str:
    if not file_path.exists():
        return None
    photo: FSInputFile = FSInputFile(file_path)
    message = await bot.send_photo(chat_id=111111111, photo=photo)

    photo_id = message.photo[-1].file_id
    return photo_id
