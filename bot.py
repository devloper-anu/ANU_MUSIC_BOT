import os

TELEGRAM_BOT_TOKEN = os.getenv('7380097256:AAGa0-J_aStZav0rpTK1L52fDmZZEKGTHkg')
API_ID = os.getenv('23712299')
API_HASH = os.getenv('9985ad1cd24a1030078b0b5a7cecf13b')

import subprocess
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! I'm your Music Bot.\n"
        "Use /play <song name or YouTube link> to download and receive an audio file."
    )

# /play command handler
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide a song name or YouTube link!")
        return

    query = " ".join(context.args)
    await update.message.reply_text(f"Searching for: {query}")
    output_filename = "song.mp3"

    # Build the yt-dlp command
    command = [
        "yt-dlp",
        "-x",                      # Extract audio
        "--audio-format", "mp3",   # Convert to mp3
        "-o", output_filename,     # Output filename
        f"ytsearch:{query}"        # Search on YouTube for the query
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        await update.message.reply_text("Download complete. Sending audio...")

        # Open the audio file and send it
        with open(output_filename, "rb") as audio:
            await update.message.reply_audio(audio=audio, title=query)

    except subprocess.CalledProcessError as e:
        logger.error("yt-dlp error: %s", e)
        await update.message.reply_text("An error occurred while downloading the song.")
    except Exception as e:
        logger.error("Unexpected error: %s", e)
        await update.message.reply_text("An unexpected error occurred.")
    finally:
        # Remove the file if it exists
        if os.path.exists(output_filename):
            os.remove(output_filename)

async def main() -> None:
    # Retrieve bot token from environment variable
    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("BOT_TOKEN not set in environment variables!")
        return

    # Build the application
    application = ApplicationBuilder().token(token).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))

    # Run the bot (polling)
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    import asyncio

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

