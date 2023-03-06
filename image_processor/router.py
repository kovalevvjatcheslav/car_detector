from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse

from image_processor.processor import get_np_array, decode_img, resize_img, normalize_img

router = APIRouter()


@router.post("/process_image", response_class=JSONResponse)
async def process_image(image: UploadFile, pipeline_id: int):
    data = get_np_array(await image.read())
    data = decode_img(data)
    data = resize_img(data)
    data = normalize_img(data)
    return {"ok": True}
