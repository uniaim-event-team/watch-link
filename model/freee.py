from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from model.base import BaseObject


class FreeeAuthorization(BaseObject):
    __tablename__ = 'freee_authorizations'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    application_name = Column(String(200))
    client_id = Column(String(200))
    client_secret = Column(String(200))
    webapp_auth_url = Column(String(500))
    jsapp_auth_url = Column(String(500))

    freee_access_tokens = relationship('FreeeAccessToken', back_populates='freee_authorization')


class FreeeCompany(BaseObject):
    __tablename__ = 'freee_companies'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    company_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(200))

    freee_employees = relationship('FreeeEmployee', back_populates='freee_company')


class FreeeEmployee(BaseObject):
    __tablename__ = 'freee_employees'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    wl_company_id = Column(BigInteger, ForeignKey('freee_companies.id'), nullable=False)
    emp_id = Column(String(100), unique=True, nullable=False)
    display_name = Column(String(200))

    freee_company = relationship('FreeeCompany', back_populates='freee_employees')


class FreeeAccessToken(BaseObject):
    __tablename__ = 'freee_access_tokens'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    freee_authorization_id = Column(BigInteger, ForeignKey('freee_authorizations.id'))
    access_token = Column(String(200))
    refresh_token = Column(String(200))
    freee_created_at = Column(String(100))

    freee_authorization = relationship('FreeeAuthorization', back_populates='freee_access_tokens')


class FreeeWorkRecord(BaseObject):
    __tablename__ = 'freee_work_records'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    emp_id = Column(String(100))
    date = Column(String(100))
    clock_in_at = Column(String(100))
    clock_out_at = Column(String(100))


class FreeeTimeClock(BaseObject):
    __tablename__ = 'freee_time_clocks'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    emp_id = Column(String(100))
    date = Column(String(100))
    clock_in_at = Column(String(100))
    clock_out_at = Column(String(100))


class FreeeKintai(BaseObject):
    __tablename__ = 'freee_kintais'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=current_timestamp(), onupdate=current_timestamp(), nullable=False)
    emp_id = Column(String(100))
    date = Column(String(100))
    clock_in_at = Column(String(100))
    clock_out_at = Column(String(100))
