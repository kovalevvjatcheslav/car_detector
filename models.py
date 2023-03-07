import typing as t

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

type_annotation_map = {list: JSON}

Base = declarative_base(type_annotation_map=type_annotation_map)


class Stage(Base):
    __tablename__ = "stage"

    id: Mapped[int] = mapped_column(primary_key=True)
    meth_name: Mapped[str]
    args: Mapped[t.Optional[list]]


class PipeLine(Base):
    __tablename__ = "pipeline"

    id: Mapped[int] = mapped_column(primary_key=True)


class PipeLineStage(Base):
    __tablename__ = "pipeline_stage"

    id: Mapped[int] = mapped_column(primary_key=True)
    stage_id: Mapped[int] = mapped_column(ForeignKey(Stage.id, ondelete="CASCADE"))
    pipeline_id: Mapped[int] = mapped_column(ForeignKey(PipeLine.id, ondelete="CASCADE"))
    order: Mapped[int]


class Sample(Base):
    __tablename__ = "sample"

    id: Mapped[int] = mapped_column(primary_key=True)
    pipeline_id: Mapped[int] = mapped_column(ForeignKey(PipeLine.id))
    in_data: Mapped[str]
    top_left_x: Mapped[t.Optional[int]]
    top_left_y: Mapped[t.Optional[int]]
    w: Mapped[t.Optional[int]]
    h: Mapped[t.Optional[int]]
    conf: Mapped[float]
    label: Mapped[int]
