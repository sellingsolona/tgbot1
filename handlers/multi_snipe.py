# handlers/multi_snipe.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import logging

async def multi_snipe_command(update: Update, context: CallbackContext):
    logging.info("User accessed multi snipe menu.")
    keyboard = [
        [InlineKeyboardButton("Generate Wallets", callback_data="generate_wallets")],
        [InlineKeyboardButton("Fund Wallets", callback_data="fund_wallets")],
        [InlineKeyboardButton("Paste Token Address", callback_data="paste_token_address")],
        [InlineKeyboardButton("Buy", callback_data="buy")],
        [InlineKeyboardButton("Sell", callback_data="confirm_sell")],
        [InlineKeyboardButton("Dump All", callback_data="confirm_dump")],
        [InlineKeyboardButton("Retrieve P-Keys", callback_data="retrieve_p_keys")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Multi-Snipe Menu:", reply_markup=reply_markup)
