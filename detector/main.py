from fastapi import FastAPI
import uvicorn

from config import settings
from detector.router import router
from sources import db


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await db.setup()


@app.on_event("shutdown")
async def shutdown_event():
    await db.release()


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "detector.main:app",
        host="0.0.0.0",
        port=settings.DETECTOR_PORT,
        log_level=settings.LOG_LEVEL,
        workers=settings.DETECTOR_WORKERS,
    )
