from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    String,
)
from sqlalchemy.sql.functions import current_timestamp

from model.base import BaseObject


class SlackChannel(BaseObject):
    __tablename__ = 'slack_channels'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    name = Column(String(200))
    token = Column(String(200))
    channel = Column(String(100))


class SlackUser(BaseObject):
    __tablename__ = 'slack_user'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    user = Column(String(100))
    other_name = Column(String(100))


class SlackMessage(BaseObject):
    __tablename__ = 'slack_messages'

    client_msg_id = Column(String(150), primary_key=True)
