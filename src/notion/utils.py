import httpx
from config.logging_config import logger
from notion import NOTION_API_TOKEN, NOTION_RAW_MAILHOOKS_DB

NOTION_API_HEADERS = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def insert_raw_mailhook_to_notion(from_email: str, from_contact: str, subject: str, body: str, email_received_at: str):
    logger.info(f"INSERT RAW MAILHOOK TO NOTION - {from_email} | {from_contact} | {subject} | {body} | {email_received_at}")
    payload = {
        "parent": { "database_id": NOTION_RAW_MAILHOOKS_DB },
        "properties": {
            "From Email": {
            "title": [
                {
                "text": {
                    "content": from_email
                }
                }
            ]
            },
            "From Contact": {
            "rich_text": [
                {
                "text": {
                    "content": from_contact
                }
                }
            ]
            },
            "Subject": {
            "rich_text": [
                {
                "text": {
                    "content": subject
                }
                }
            ]
            },
            "Body": {
            "rich_text": [
                {
                "text": {
                    "content": body
                }
                }
            ]
            },
            "Email Received at": {
            "date": {
                "start": email_received_at
            }
            }
        }
    }
    response = httpx.post(
        url="https://api.notion.com/v1/pages",
        headers=NOTION_API_HEADERS,
        json=payload
    )
    status_code = response.status_code
    logger.info(f"STATUS CODE - {status_code}")
    if status_code == 200:
        logger.debug(response.json())
        return True
    else:
        logger.error(f"!!! FAILED INSERTING - {response.text}")
    