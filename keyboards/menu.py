from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def get_main_menu() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Generate QR"), KeyboardButton(text="History")],
        [KeyboardButton(text="Help"), KeyboardButton(text="About")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_qr_types_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(text="URL 🔗", callback_data="qr_type_url"),
            InlineKeyboardButton(text="Text 📝", callback_data="qr_type_text"),
        ],
        [
            InlineKeyboardButton(text="Wi-Fi 📶", callback_data="qr_type_wifi"),
            InlineKeyboardButton(text="Contact 📇", callback_data="qr_type_contact"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
