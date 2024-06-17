from config.database import postgres
from config.logging_config import logger


def sql_p_save_mailhook(from_email: str, subject: str, body: str, email_received_at: str) -> bool:
    logger.info(f"SAVE MAILHOOK TO DB (Postgres) - {from_email} | {subject} | {body} | {email_received_at}")
    query = f"""
    INSERT INTO raw_mailhooks 
    (
        from_email,
        subject,
        body,
        email_received_at
    ) 
        VALUES
    (
        '{from_email}',
        '{subject}',
        '{body}',
        '{email_received_at}'
    )
    """
    insert_result = postgres.execute_with_connection(
        func=postgres.insert_executor,
        query=query
    )
    return insert_result
