import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

API_TOKEN = '7808996327:AAG-gViuxnNhj3kiKQVLxDc7dGkSRH7oJjM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello! I'm your music bot.")

async def on_start():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(on_start())


# Logging setup
logging.basicConfig(level=logging.INFO)

# Environment Variables (Render pe set karna)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Ensure token exists
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Start command
@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.reply("🎵 Welcome to the Telegram Music Bot! Send a song name to search.")

# Help command
@dp.message_handler(commands=['help'])
async def help_command(message: Message):
    await message.reply("🎵 Use /start to begin and send a song name to search for music!")

# Handle text messages
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_music_request(message: Message):
    await message.reply(f"🔍 Searching for: {message.text} (Feature Coming Soon!)")

# Main function
async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
