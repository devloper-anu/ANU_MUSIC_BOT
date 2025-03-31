from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Environment variable se token lena best practice hai

async def start(update: Update, context):
    await update.message.reply_text("Hello! I'm your Music Bot 🎵")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
