from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from .forms import AddDiscordID, EditDB
from aiogram.types import FSInputFile
from ....database.db import DB
import pandas as pd

callbacks = Router()
db = DB()

@callbacks.callback_query()
async def button_callbacks(callback: CallbackQuery, state: FSMContext):
    match callback.data:
        case "add_discord_channel":
            await state.set_state(AddDiscordID.discord_id)
            await callback.message.answer("Введите ID Discord канала:")
        case "upload_db":
            for i, collection in enumerate(db.get_all_info()):
                df = pd.DataFrame(collection)
                df.to_excel(f"collecion_{i}.xlsx")
                await callback.message.answer_document(document=FSInputFile(f"colection_{i}.xlsx"))
        case "edit_db":
            await state.set_state(EditDB.file)