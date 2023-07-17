from aiogram.types import CallbackQuery
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from .forms import AddDiscordID
from ...discord_bot.bot import bot as ds_bot
from ...telegram_bot.bot import bot as tg_bot

add_discord = Router()


@add_discord.message(AddDiscordID.discord_id)
async def process_discord_id(message: Message, state: FSMContext):
    await state.set_state(AddDiscordID.telegram_id)
    if message.text.isnumeric():
        channel = ds_bot.get_channel(int(message.text))
        if channel:
            channel_name = channel.name
        await message.reply(f"Вы успешно добавили канал {channel_name}! Теперь введите ID Telegram канала:")

@add_discord.message(AddDiscordID.telegram_id)
async def process_telegram_id(message: Message, state: FSMContext):
    await state.clear()
    if message.text.isnumeric():
        channel = await tg_bot.get_chat(int(message.text))
        await message.reply(f"Вы успешно связали с каналом {channel.title}!")
