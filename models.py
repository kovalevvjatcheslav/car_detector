from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


Base = declarative_base()


class Stage(Base):
    __tablename__ = "stage"

    id: Mapped[int] = mapped_column(primary_key=True)


class PipeLine(Base):
    __tablename__ = "pipeline"

    id: Mapped[int] = mapped_column(primary_key=True)


class PipeLineStage(Base):

    __tablename__ = "pipeline_stage"

    id: Mapped[int] = mapped_column(primary_key=True)
    stage_id: Mapped[int] = mapped_column(ForeignKey(Stage.id))
    pipeline_id: Mapped[int] = mapped_column(ForeignKey(PipeLine.id))
