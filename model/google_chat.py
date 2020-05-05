from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    String,
)
from sqlalchemy.sql.functions import current_timestamp

from model.base import BaseObject


class GoogleChatWebhook(BaseObject):
    __tablename__ = 'google_chat_webhook'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    name = Column(String(200))
    url = Column(String(500))
