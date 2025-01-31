# handlers/bundler.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import logging

async def bundler_command(update: Update, context: CallbackContext):
    logging.info("User accessed bundler menu.")
    keyboard = [
        [InlineKeyboardButton("Generate Wallets", callback_data="generate_wallets")],
        [InlineKeyboardButton("Fund Wallets", callback_data="fund_wallets")],
        [InlineKeyboardButton("Create Token", callback_data="create_token")],
        [InlineKeyboardButton("Dump All", callback_data="confirm_dump")],
        [InlineKeyboardButton("Sell", callback_data="confirm_sell")],
        [InlineKeyboardButton("Retrieve P-Keys", callback_data="retrieve_p_keys")],
        [InlineKeyboardButton("Check Balances", callback_data="check_balances")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bundler Menu:", reply_markup=reply_markup)
