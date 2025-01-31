# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot API Key
BOT_API_KEY = os.getenv("BOT_API_KEY")
if not BOT_API_KEY:
    raise ValueError("BOT_API_KEY environment variable is not set")

# Encryption Key
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    raise ValueError("ENCRYPTION_KEY environment variable is not set")
