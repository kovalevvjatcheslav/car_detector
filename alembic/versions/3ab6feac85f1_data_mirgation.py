"""data mirgation

Revision ID: 3ab6feac85f1
Revises: 8d91b675e7f9
Create Date: 2023-03-07 20:44:11.167636

"""
from alembic import op
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from models import Stage, PipeLine, PipeLineStage


# revision identifiers, used by Alembic.
revision = "3ab6feac85f1"
down_revision = "8d91b675e7f9"
branch_labels = None
depends_on = None

METHODS = ["to_np_array", "decode_img", "resize_img", "normalize_img", "to_base64"]


def upgrade() -> None:
    pipeline_stages = []

    with Session(bind=op.get_bind()) as session:
        pipeline = PipeLine()
        session.add(pipeline)
        session.commit()
        order = 1

        for method in METHODS:
            stage = Stage(meth_name=method)
            session.add(stage)
            session.commit()
            pipeline_stages.append(
                PipeLineStage(stage_id=stage.id, pipeline_id=pipeline.id, order=order)
            )
            order += 1

        session.add_all(pipeline_stages)


def downgrade() -> None:
    with Session(bind=op.get_bind()) as session:
        pipeline_ids = set(
            session.scalars(
                select(PipeLineStage.pipeline_id).join(Stage).where(Stage.meth_name.in_(METHODS))
            )
        )
        session.execute(delete(Stage).where(Stage.meth_name.in_(METHODS)))
        session.execute(delete(PipeLine).where(PipeLine.id.in_(pipeline_ids)))
