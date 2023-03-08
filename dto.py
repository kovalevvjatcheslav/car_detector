import typing as t

from pydantic import BaseModel


class StageDTO(BaseModel):
    meth_name: str
    args: t.List[t.Optional[t.Any]]


class PipeLineDTO(BaseModel):
    pipeline_id: int
    stages: t.List[StageDTO]


class SampleDTO(BaseModel):
    top_left_x: t.Optional[int]
    top_left_y: t.Optional[int]
    w: t.Optional[int]
    h: t.Optional[int]
    conf: float
    label: int


class DetectorInput(BaseModel):
    pipeline_id: int
    data: str
