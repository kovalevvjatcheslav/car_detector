from fastapi import APIRouter
from fastapi.responses import JSONResponse

from dto import DetectorInput
from detector.utils import detect_car

router = APIRouter()


@router.post("/detect", response_class=JSONResponse)
async def process_image(payload: DetectorInput):
    return (await detect_car(payload)).dict(exclude_none=True)
