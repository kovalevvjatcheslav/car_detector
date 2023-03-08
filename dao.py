import typing as t

from sqlalchemy import select

from dto import PipeLineDTO, StageDTO, SampleDTO
from models import PipeLineStage, Stage, Sample
from sources import db


class PipeLineDAO:
    @staticmethod
    async def get_all() -> t.List[PipeLineDTO]:
        async with db.session_maker() as session:
            result = {}
            for pipeline_id, meth_name, args in await session.execute(
                select(PipeLineStage.pipeline_id, Stage.meth_name, Stage.args)
                .join(Stage)
                .order_by(PipeLineStage.order)
            ):
                stage = StageDTO(meth_name=meth_name, args=args if args else [])

                if pipeline_id in result:
                    result[pipeline_id].stages.append(stage)
                else:
                    result[pipeline_id] = PipeLineDTO(pipeline_id=pipeline_id, stages=[stage])
        return list(result.values())

    @staticmethod
    async def get_by_id(pipeline_id: int) -> t.Optional[PipeLineDTO]:
        async with db.session_maker() as session:
            stages = []
            for meth_name, args in await session.execute(
                select(Stage.meth_name, Stage.args)
                .join(PipeLineStage)
                .order_by(PipeLineStage.order)
                .where(PipeLineStage.pipeline_id == pipeline_id)
            ):
                stages.append(StageDTO(meth_name=meth_name, args=args if args else []))
        if not stages:
            return
        return PipeLineDTO(pipeline_id=pipeline_id, stages=stages)


class SampleDAO:
    @staticmethod
    async def create_sample(data: str, pipeline_id: int, sample_dto: SampleDTO):
        async with db.session_maker() as session:
            sample = Sample(
                pipeline_id=pipeline_id, in_data=data, **sample_dto.dict(exclude_none=True)
            )
            session.add(sample)
            await session.commit()
