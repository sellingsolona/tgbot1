# handlers/general.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import logging
from utils.confirmation import generate_confirmation_buttons
import requests

async def homepage_command(update: Update, context: CallbackContext):
    """Displays the main menu with options."""
    logging.info("User accessed homepage menu.")
    keyboard = [
        [InlineKeyboardButton("Bundler", callback_data="bundler")],
        [InlineKeyboardButton("Multi Snipe", callback_data="multi_snipe")],
        [InlineKeyboardButton("Check Wallet Balances", callback_data="check_balances")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select an option:", reply_markup=reply_markup)

async def confirm_action(update: Update, context: CallbackContext):
    """Handles confirmation actions for various commands."""
    query = update.callback_query
    action = query.data.split('_')[1]
    logging.info(f"User confirmed action: {action}")

    if action == "dump":
        await query.message.reply_text("Dumping all tokens...")
        logging.info("Executing dump all tokens logic.")
    elif action == "sell":
        await query.message.reply_text("Selling tokens...")
        logging.info("Executing sell tokens logic.")
    elif action == "create_token":
        user_data = context.user_data
        response = requests.post("https://pump.fun/api/create_token", json=user_data)

        if response.status_code == 200:
            await query.message.reply_text("Token successfully created!")
            logging.info("Token creation successful.")
        else:
            await query.message.reply_text("Failed to create token. Please try again.")
            logging.error("Token creation failed.")
        user_data.clear()

    await query.answer()
