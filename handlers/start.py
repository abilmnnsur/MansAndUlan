from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keyboards.menu import get_main_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот для генерации QR-кодов. Используй меню ниже:",
        reply_markup=get_main_menu(),
    )


@router.message(F.text == "Help")
@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Нажми 'Generate QR', выбери тип данных, отправь текст и получи картинку!"
    )


@router.message(F.text == "About")
async def cmd_about(message: Message):
    await message.answer("Курсовой проект.\nСтек: aiogram 3.x, requests, OOP, JSON.")
