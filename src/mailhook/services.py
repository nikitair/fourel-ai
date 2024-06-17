from config.logging_config import logger
# from dataclasses import dataclass
from mailhook import schemas
from mailhook import utils


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
    
    # save mailhook
    save_result = utils.sql_p_save_mailhook(
        from_email=email,
        from_contact=contact,
        subject=subject,
        body=body,
        email_received_at=email_received_at
    )
    if save_result:
        result["success"] = True
        logger.info(f"MAILHOOK SAVED")
    return result