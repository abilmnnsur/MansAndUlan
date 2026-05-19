from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.menu import get_main_menu   # ← ДОБАВИТЬ

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для генерации QR-кодов. Выбери действие.",
        reply_markup=get_main_menu()
    )