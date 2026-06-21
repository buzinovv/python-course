import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я твой первый бот 🎉")
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(f"{message.from_user.first_name}, вот список всех доступных команд:\n"
                         f"/start - Приветствие\n"
                         f"/help - Список команд"
                         )
async def main():
    await dp.start_polling(bot)

asyncio.run(main())