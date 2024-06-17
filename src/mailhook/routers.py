from fastapi import APIRouter, Request
from config.logging_config import logger
from mailhook import schemas


router = APIRouter()


@router.get("/")
async def mailhook_index():
    logger.info("*** MAILHOOK INDEX TRIGGERED")
    return {"service": "Fourel AI", "router": "Mailhook"}


@router.post("/")
async def mailhook(request: schemas.MailHook) -> schemas.MailHookResponse:
    logger.info("*** MAILHOOK TRIGGERED")
    request_dict = dict(request)
    logger.info(f"RAW PAYLOAD - {request_dict}")
    return {"success": True, "payload": request_dict}
