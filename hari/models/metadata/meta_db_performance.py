import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB 

from datetime import datetime


from models.metadata.meta_db import MetaDB


class MetaDbPerformance(MetaDB):

    __tablename__ = 'meta_db_performance'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    job_name: str = sa.Column(sa.String(80), unique=False, nullable=False)
    # job_metric: str = sa.Column(JSONB, nullable=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now(), nullable=False)
    updated_at = sa.Column(sa.DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
