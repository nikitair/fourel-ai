from fastapi import APIRouter, Request
from config.logging_config import logger


router = APIRouter()


@router.get("/")
async def mailhook_index():
    logger.info("*** MAILHOOK INDEX TRIGGERED")
    return {"service": "Fourel AI", "router": "Mailhook"}


@router.post("/echo")
async def mailhook_echo(request: Request):
    logger.info("*** MAILHOOK ECHO TRIGGERED")
    request_dict = request.__dict__()
    return request_dict


@router.post("/")
async def mailhook_echo(request: Request):
    logger.info("*** MAILHOOK TRIGGERED")
    return {"messages": "Under Development"}
