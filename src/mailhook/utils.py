from config.database import postgres
from config.logging_config import logger
import re


def sql_p_save_mailhook(from_email: str, from_contact: str, subject: str, body: str, email_received_at: str) -> bool:
    logger.info(f"SAVE MAILHOOK TO DB (Postgres) - {from_email} | {from_contact} | {subject} | {body} | {email_received_at}")
    query = f"""
    INSERT INTO raw_mailhooks 
    (
        from_email,
        from_contact,
        subject,
        body,
        email_received_at
    ) 
        VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s
    )
    """
    insert_result = postgres.execute_with_connection(
        func=postgres.insert_executor,
        query=query,
        params=[(from_email, from_contact, subject, body, email_received_at)]
    )
    return insert_result


def format_email_sender(email_sender: str) -> tuple:
    """
    Nikita <nikita@actse.ltd> -> ('Nikita', 'nikita@actse.ltd')
    """
    logger.info(f"FORMAT EMAIL SENDER - {email_sender}")
    match = re.match(r'^(.*)\s<(.+@.+)>$', email_sender)
    if match:
        name, email = match.groups()
        return (name, email)
    else:
        return(email_sender, '')
