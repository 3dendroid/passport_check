import os
import subprocess

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Send /start_test to start the test.")


async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Bot for checking passport status. Please select /check_status to check status.")
    try:
        result = subprocess.run(
            ["pytest", "tests/test_pass_check.py", "-sv"],
            capture_output=True, text=True, timeout=120
        )
        await update.message.reply_text(f"✅ Test completed:\n\n{result.stdout[-3000:]}")
    except Exception as e:
        # Send error to telegram
        await update.message.reply_text(f"❌ Error:\n{str(e)}")


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check_status", start_test))
    print("Bot is running...")
    app.run_polling()
