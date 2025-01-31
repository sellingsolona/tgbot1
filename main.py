# main.py
import logging
from telegram.ext import ApplicationBuilder
from config import BOT_API_KEY
from handlers import register_handlers

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Application
app = ApplicationBuilder().token(BOT_API_KEY).build()

# Register handlers
register_handlers(app)

if __name__ == '__main__':
    app.run_polling()
