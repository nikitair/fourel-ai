from fastapi import FastAPI
import uvicorn
from config.logging_config import logger
from mailhook.routers import router as mailhook_router


app = FastAPI()

# register routers
app.include_router(router=mailhook_router, prefix="mailhook", tags=["mailhook"])


@app.get("/")
async def index():
    logger.info("*** FOUREL AI INDEX TRIGGERED")
    return {"service": "Fourel AI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
