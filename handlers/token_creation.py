# handlers/token_creation.py
from telegram import Update
from telegram.ext import CallbackContext
import logging
from utils.confirmation import generate_confirmation_buttons

async def create_token_command(update: Update, context: CallbackContext):
    logging.info("User started token creation process.")
    await update.message.reply_text("Enter token name:")
    context.user_data["awaiting_token_name"] = True

async def process_token_details(update: Update, context: CallbackContext):
    user_input = update.message.text
    user_data = context.user_data
    logging.info(f"User provided input: {user_input}")

    if "awaiting_token_name" in user_data:
        user_data["token_name"] = user
