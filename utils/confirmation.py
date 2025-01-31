# utils/confirmation.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def generate_confirmation_buttons(action):
    """Creates Yes/No confirmation buttons for a given action."""
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data=f"confirm_{action}"), 
         InlineKeyboardButton("No", callback_data="cancel")]
    ]
    return InlineKeyboardMarkup(keyboard)
