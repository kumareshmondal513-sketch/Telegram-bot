
import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from flask import Flask
import threading
app = Flask(__name__)
@app.route('/health')
def health(): return "OK", 200
    def run_flask()
app.run(host='0.0.0.0', port=5000)
# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://your-frontend-url.netlify.app")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "Open Mini App", 
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to Tap Rewards Bot! Click below to launch the app:",
        reply_markup=reply_markup
    )

def run_bot():
    if not BOT_TOKEN:
        print("BOT_TOKEN is missing!")
        return

    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start
    application.run_polling()

if __name__ == '__main__':
    run_bot()
