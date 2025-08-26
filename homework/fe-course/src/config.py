import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file."""
    load_dotenv()

def get_key(key: str, default=None):
    """Fetch a key from environment variables."""
    return os.getenv(key, default)


# Quick test when running directly
if __name__ == "__main__":
    load_env()
    print("API_KEY:", get_key("API_KEY"))
    print("DATA_DIR:", get_key("DATA_DIR"))
