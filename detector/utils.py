import random

from dao import SampleDAO
from dto import SampleDTO, DetectorInput


async def detect_car(payload: DetectorInput) -> SampleDTO:
    conf = random.random()
    result = {"conf": conf}
    if conf > 0.5:
        result["top_left_x"] = 42
        result["top_left_y"] = 42
        result["w"] = 100500
        result["h"] = 100500
        result["label"] = 1
    else:
        result["label"] = 0
    sample_dto = SampleDTO(**result)
    await SampleDAO.create_sample(**payload.dict(), sample_dto=sample_dto)
    return sample_dto
