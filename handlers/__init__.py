# handlers/__init__.py
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters
from .bundler import bundler_command
from .multi_snipe import multi_snipe_command
from .token_creation import create_token_command, process_token_details
from .general import homepage_command, confirm_action

def register_handlers(app):
    app.add_handler(CommandHandler('start', homepage_command))
    app.add_handler(CommandHandler('bundler', bundler_command))
    app.add_handler(CommandHandler('multi_snipe', multi_snipe_command))
    app.add_handler(CommandHandler('create_token', create_token_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_token_details))
    app.add_handler(CallbackQueryHandler(confirm_action, pattern='^confirm_'))
