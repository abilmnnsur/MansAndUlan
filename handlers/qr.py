from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.menu import get_qr_types_menu
from services.qr_service import QRService
from services.file_manager import FileManager
from config import HISTORY_FILE
from models.url_qr import URLQR
from models.text_qr import TextQR
from models.wifi_qr import WifiQR
from models.contact_qr import ContactQR
from utils.validators import validate_input, validate_split_input

router = Router()
file_manager = FileManager(HISTORY_FILE)

class QRForm(StatesGroup):
    choosing_type = State()
    waiting_data = State()


@router.message(F.text == "Generate QR")
async def process_generate_button(message: Message, state: FSMContext):
    await state.set_state(QRForm.choosing_type)
    await message.answer("Выберите тип QR-кода:", reply_markup=get_qr_types_menu())

@router.message(F.text == "Help")
async def cmd_help(message: Message):
    await message.answer("🛠 Помощь: выбери 'Generate QR' и следуй подсказкам для создания кода.")

@router.message(F.text == "About")
async def cmd_about(message: Message):
    await message.answer("ℹ️ QR-Генератор v1.0\nРазработчики: Mans & Ulan")

@router.callback_query(QRForm.choosing_type, F.data.startswith("qr_type_"))
async def type_callback(callback: CallbackQuery, state: FSMContext):
    qr_type = callback.data.split("_")[2]
    await state.update_data(chosen_type=qr_type)
    await state.set_state(QRForm.waiting_data)

    prompts = {
        "url": "Отправьте ссылку (например, yandex.ru):",
        "text": "Отправьте любой текст:",
        "wifi": "Отправьте имя сети и пароль через запятую (Пример: MyWifi,12345):",
        "contact": "Отправьте Имя и Телефон через запятую (Пример: Иван, +79991112233):",
    }
    await callback.message.edit_text(prompts[qr_type])
    await callback.answer()

@router.message(QRForm.waiting_data)
async def data_received(message: Message, state: FSMContext):
    if not validate_input(message.text):
        await message.answer("Ввод не должен быть пустым.")
        return

    user_data = await state.get_data()
    qr_type = user_data.get("chosen_type")
    text = message.text

    try:
        if qr_type == "url":
            qr_obj = URLQR(text)
        elif qr_type == "text":
            qr_obj = TextQR(text)
        elif qr_type in ["wifi", "contact"]:
            if not validate_split_input(text):
                await message.answer("Ошибка формата. Используйте запятую как разделитель.")
                return
            p1, p2 = [p.strip() for p in text.split(",")]
            qr_obj = WifiQR(p1, p2) if qr_type == "wifi" else ContactQR(p1, p2)

        await message.answer("⏳ Генерация...")
        img_bytes = await QRService.generate(qr_obj)

        photo = BufferedInputFile(img_bytes, filename="qr.png")
        await message.answer_photo(photo, caption=f"Готово! Тип: {qr_obj.get_type()}")

        file_manager.save_record(message.from_user.id, qr_obj.get_type(), text)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
    finally:
        await state.clear()