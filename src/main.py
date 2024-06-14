from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def index():
    return {"service": "Fourel AI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
