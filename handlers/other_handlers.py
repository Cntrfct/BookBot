from aiogram import Router
from aiogram.types import Message

router = Router()


# Этот хендлер будет реагировать на любые сообщения,
# не предусмотренные логикой работы бота
@router.message()
async def send_unknown(message: Message):
    await message.answer('Я не знаю таких команд! Отправьте /help')
