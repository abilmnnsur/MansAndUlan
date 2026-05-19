from aiogram import Router, F
from aiogram.types import Message
from services.file_manager import FileManager
from config import HISTORY_FILE
from datetime import datetime

router = Router()
file_manager = FileManager(HISTORY_FILE)


@router.message(F.text == "History")
async def show_history(message: Message):
    records = file_manager.get_user_history(message.from_user.id, limit=5)
    if not records:
        await message.answer("История пуста.")
        return

    res = "📋 Последние 5 QR-кодов:\n\n"
    for idx, r in enumerate(records, start=1):
        dt = datetime.fromisoformat(r["timestamp"]).strftime("%d.%m %H:%M")
        res += f"{idx}. [{r['qr_type']}] {r['content'][:20]}\n⏱ {dt}\n\n"
    await message.answer(res)
