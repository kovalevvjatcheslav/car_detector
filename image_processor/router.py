from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import httpx

from config import settings
from dao import PipeLineDAO
from image_processor.processor import Pipeline


router = APIRouter()


@router.post("/process_image", response_class=JSONResponse)
async def process_image(image: UploadFile, pipeline_id: int):
    pipeline_dto = await PipeLineDAO.get_by_id(pipeline_id)
    if not pipeline_dto:
        raise HTTPException(status_code=404, detail="Pipeline not found")

    data = Pipeline.run(
        await image.read(),
        pipeline_dto.stages,
    )
    async with httpx.AsyncClient() as client:
        request_data = {"pipeline_id": pipeline_id, "data": data}
        response = await client.post(
            f"http://{settings.DETECTOR_HOST}:{settings.DETECTOR_PORT}/detect", json=request_data
        )
        return response.json()


@router.get("/pipelines", response_class=JSONResponse)
async def process_image():
    return await PipeLineDAO.get_all()
