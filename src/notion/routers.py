from fastapi import APIRouter
from config.logging_config import logger
from notion import schemas
from notion import services

router = APIRouter()


@router.get("/")
async def notion_index():
    logger.info("*** NOTION INDEX TRIGGERED")
    return {"service": "Fourel AI", "router": "Notion"}

