import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# === Paste your bot token here ===
BOT_TOKEN = "7723526275:AAGHR8u6pY4w41gr35ApTjPX_mAY--FSTPE"

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Tài xỉu command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Chào mừng đến với bot Tài Xỉu!\nGõ /taixiu để chơi thử nhé."
    )

async def taixiu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = random.randint(3, 18)
    outcome = "Tài" if result >= 11 else "Xỉu"
    await update.message.reply_text(
        f"Kết quả: {result} → {outcome}"
    )

# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("taixiu", taixiu))

    print("Bot đang chạy...")
    app.run_polling()