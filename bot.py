import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

logging.basicConfig(level=logging.INFO)

CHANNELS = [
    {
        "section": "🏠 בית וטכנולוגיה",
        "items": [
            {"name": "🏠 Smart Home & LED",         "url": "https://t.me/SMARTHOMELEDS"},
            {"name": "💻 מחשבים וגאדג'טים",         "url": "https://t.me/COMPUTERACCESSO"},
            {"name": "🚗 גאדג'טים לרכב & Dash Cam", "url": "https://t.me/CARSGAD"},
        ]
    },
    {
        "section": "🏃 ספורט ופנאי",
        "items": [
            {"name": "💪 כושר וספורט",              "url": "https://t.me/FITANDNESS"},
            {"name": "⛺ קמפינג וטיולים",            "url": "https://t.me/CAMPINGSHOPPING"},
            {"name": "🌱 גינון וצמחים",              "url": "https://t.me/GARDENINGSS"},
        ]
    },
    {
        "section": "👕 אופנה",
        "items": [
            {"name": "👗 ביגוד נשים",               "url": "https://t.me/CLOTHSWOMENS"},
            {"name": "👔 ביגוד גברים",               "url": "https://t.me/CLOTHSMENS"},
        ]
    },
    {
        "section": "👶 ילדים ומשפחה",
        "items": [
            {"name": "👶 תינוקות ופעוטות",           "url": "https://t.me/BABIESSTUFFS"},
        ]
    },
]

def build_keyboard():
    keyboard = []
    for section in CHANNELS:
        keyboard.append([
            InlineKeyboardButton(f"── {section['section']} ──", callback_data="noop")
        ])
        row = []
        for i, item in enumerate(section["items"]):
            row.append(InlineKeyboardButton(item["name"], url=item["url"]))
            if len(row) == 2 or i == len(section["items"]) - 1:
                keyboard.append(row)
                row = []
    return InlineKeyboardMarkup(keyboard)

WELCOME_TEXT = (
    "🛍 ברוכים הבאים ל-AliPlus IL!\n\n"
    "כל הדילים מעלי אקספרס במקום אחד ✨\n"
    "בחרו קטגוריה והצטרפו לערוץ הרלוונטי 👇"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text=WELCOME_TEXT,
        reply_markup=build_keyboard()
    )

async def noop_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(noop_handler, pattern="^noop$"))
    print("AliPlus Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
