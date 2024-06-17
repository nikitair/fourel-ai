import os
from dotenv import load_dotenv

load_dotenv()

NOTION_RAW_MAILHOOKS_DB = os.getenv("NOTION_RAW_MAILHOOKS_DB", "")
NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN", "")
