from config.logging_config import logger
# from dataclasses import dataclass
from mailhook import schemas
from mailhook import utils
from notion import utils as notion_utils


def mailhook(payload: schemas.MailHook):
    result = {
        "success": False,
        "payload": dict(payload)
    }
    logger.info(f"MAILHOOK RECEIVED - {dict(payload)}")
    sender = payload.sender
    subject = payload.subject
    body = payload.body
    email_received_at = payload.date
    
    # get email and contact
    contact, email = utils.format_email_sender(sender)
    logger.info(f"EMAIL - {email}; CONTACT - {contact}")
    
    # save mailhook to Notion
    notion_save_result = notion_utils.insert_raw_mailhook_to_notion(
        from_email=email,
        from_contact=contact,
        subject=subject,
        body=body,
        email_received_at=email_received_at
    )
    logger.info(f"IS SAVED TO NOTION - {notion_save_result} ")
    
    # save mailhook to db
    db_save_result = utils.sql_p_save_mailhook(
        from_email=email,
        from_contact=contact,
        subject=subject,
        body=body,
        email_received_at=email_received_at
    )
    logger.info(f"IS SAVED TO DB - {db_save_result} ")
    
    if any((notion_save_result, db_save_result)):
        result["success"] = True
        logger.info(f"MAILHOOK SAVED")
    return result
