from sqlalchemy import (
    BigInteger,
    Integer,
    Column,
    DateTime,
    Text,
    String,
)
from sqlalchemy.sql.functions import current_timestamp

from model.base import BaseObject


class WatchLink(BaseObject):
    __tablename__ = 'watch_links'

    RESERVE_TYPE_EVERY = 1
    RESERVE_TYPE_DAILY = 2

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    name = Column(String(100))
    reserve_type = Column(Integer)
    reserve_hm = Column(String(4))
    watch_table = Column(String(100))
    watch_id = Column(BigInteger)
    link_table = Column(String(100))
    link_id = Column(BigInteger)


class WatchLog(BaseObject):
    __tablename__ = 'watch_logs'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    watch_link_id = Column(BigInteger)
    message = Column(Text)
