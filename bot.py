import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

logging.basicConfig(level=logging.INFO)

CHANNELS = [
    {"name": "🏠 Smart Home & LED",          "url": "https://t.me/SMARTHOMELEDS"},
    {"name": "💻 מחשבים וגאדג'טים",          "url": "https://t.me/COMPUTERACCESSO"},
    {"name": "🚗 גאדג'טים לרכב & Dash Cam",  "url": "https://t.me/CARSGAD"},
    {"name": "💪 כושר וספורט",               "url": "https://t.me/FITANDNESS"},
    {"name": "⛺ קמפינג וטיולים",             "url": "https://t.me/CAMPINGSHOPPING"},
    {"name": "🌱 גינון וצמחים",               "url": "https://t.me/GARDENINGSS"},
    {"name": "👗 ביגוד נשים",                "url": "https://t.me/CLOTHSWOMENS"},
    {"name": "👔 ביגוד גברים",                "url": "https://t.me/CLOTHSMENS"},
    {"name": "👶 תינוקות ופעוטות",            "url": "https://t.me/BABIESSTUFFS"},
]

def build_keyboard():
    keyboard = []
    row = []
    for i, ch in enumerate(CHANNELS):
        row.append(InlineKeyboardButton(ch["name"], url=ch["url"]))
        if len(row) == 2 or i == len(CHANNELS) - 1:
            keyboard.append(row)
            row = []
    return InlineKeyboardMarkup(keyboard)

WELCOME_TEXT = (
    "🛍 ברוכים הבאים ל-AliPlus IL!\n\n"
    "כל הדילים מעלי אקספרס במקום אחד\n"
    "בחרו קטגוריה והצטרפו לערוץ הרלוונטי 👇"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text=WELCOME_TEXT,
        reply_markup=build_keyboard()
    )

async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("AliPlus Bot is running...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
