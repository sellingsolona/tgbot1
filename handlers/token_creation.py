# handlers/token_creation.py
from telegram import Update
from telegram.ext import CallbackContext
import logging
from utils.confirmation import generate_confirmation_buttons

async def create_token_command(update: Update, context: CallbackContext):
    """Initiates the token creation process."""
    logging.info("User started token creation process.")
    await update.message.reply_text("Enter token name:")
    context.user_data["awaiting_token_name"] = True

async def process_token_details(update: Update, context: CallbackContext):
    """Handles user input for token creation."""
    user_input = update.message.text
    user_data = context.user_data
    logging.info(f"User provided input: {user_input}")

    if "awaiting_token_name" in user_data:
        user_data["token_name"] = user_input
        del user_data["awaiting_token_name"]
        await update.message.reply_text("Enter token symbol:")
        user_data["awaiting_token_symbol"] = True
    elif "awaiting_token_symbol" in user_data:
        user_data["token_symbol"] = user_input
        del user_data["awaiting_token_symbol"]
        await update.message.reply_text("Enter supply:")
        user_data["awaiting_supply"] = True
    elif "awaiting_supply" in user_data:
        user_data["supply"] = user_input
        del user_data["awaiting_supply"]
        await update.message.reply_text("Enter decimals:")
        user_data["awaiting_decimals"] = True
    elif "awaiting_decimals" in user_data:
        user_data["decimals"] = user_input
        del user_data["awaiting_decimals"]
        await update.message.reply_text("Enter website (or type 'none'):")
        user_data["awaiting_website"] = True
    elif "awaiting_website" in user_data:
        user_data["website"] = user_input
        del user_data["awaiting_website"]
        await update.message.reply_text("Enter Telegram (or type 'none'):")
        user_data["awaiting_telegram"] = True
    elif "awaiting_telegram" in user_data:
        user_data["telegram"] = user_input
        del user_data["awaiting_telegram"]
        await update.message.reply_text("Enter Twitter (or type 'none'):")
        user_data["awaiting_twitter"] = True
    elif "awaiting_twitter" in user_data:
        user_data["twitter"] = user_input
        del user_data["awaiting_twitter"]
        logging.info("Token creation details collected. Awaiting confirmation.")
        await update.message.reply_text("Confirm token creation:", reply_markup=generate_confirmation_buttons("create_token"))
