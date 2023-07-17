from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_keyboard =InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Выгрузить БД", callback_data="upload_db"), 
        InlineKeyboardButton(text="Изменить БД", callback_data="change_db")], 
    ]
)