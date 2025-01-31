# config.py
import os

# Load environment variables
BOT_API_KEY = os.getenv("BOT_API_KEY")
if not BOT_API_KEY:
    raise ValueError("BOT_API_KEY environment variable is not set")

ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    raise ValueError("ENCRYPTION_KEY environment variable is not set")
