# database.py
import sqlite3

DB_PATH = "data/wallets.db"

def init_db():
    """Initializes the database and creates the wallets table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS wallets (
                 id INTEGER PRIMARY KEY, 
                 address TEXT, 
                 private_key TEXT)''')
    conn.commit()
    conn.close()

def insert_wallet(address, private_key):
    """Inserts a new wallet into the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO wallets (address, private_key) VALUES (?, ?)", (address, private_key))
    conn.commit()
    conn.close()

def get_wallets():
    """Retrieves all wallets from the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM wallets")
    wallets = c.fetchall()
    conn.close()
    return wallets

# Initialize the database
init_db()
