import logging
from telegram.ext import Application, CommandHandler

# Replace with your bot's token
TELEGRAM_BOT_TOKEN = "7380097256:AAGa0-J_aStZav0rpTK1L52fDmZZEKGTHkg"

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                       level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a command handler
async def start(update, context):
    await update.message.reply_text("Hello! I'm your bot.")

async def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handler
    application.add_handler(CommandHandler("start", start))

    # Run polling without asyncio.run
    await application.run_polling()

if __name__ == "__main__":
    # Start the bot
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
