import json
import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env file
dotenv_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# secret = os.getenv("SECRET")
