from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Добавить Discord канал", callback_data="add_discord_channel")],
        [InlineKeyboardButton(text="Добавить Telegram канал", callback_data="add_telegram_channel")],
        [InlineKeyboardButton(text="Реферальная система", callback_data="ref_system")]
    ]
)