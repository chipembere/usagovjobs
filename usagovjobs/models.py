from typing import Any
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from usagovjobs import constants

Base = declarative_base()


class DataAnalyst(Base):
    __tablename__ = "data_analyst"

    def __init__(self, table_name: str, *args: Any, **kwargs: Any) -> None:
        __tablename__ = table_name
        super().__init__(*args, **kwargs)

    id = Column(Integer, primary_key=True, nullable=False)
    position_id = Column(String(256), unique=True, nullable=False)
    position_title = Column(String(256), nullable=False)
    organization_name = Column(String(256), nullable=False)
    min_salary = Column(Float, nullable=False)
    max_salary = Column(Float, nullable=False)
    salary_interval = Column(String(20), nullable=False)
    who_may_apply = Column(String(63))


class DataScientist(Base):
    __tablename__ = "data_scientist"

    def __init__(self, table_name: str, *args: Any, **kwargs: Any) -> None:
        __tablename__ = table_name
        super().__init__(*args, **kwargs)

    id = Column(Integer, primary_key=True, nullable=False)
    position_id = Column(String(256), unique=True, nullable=False)
    position_title = Column(String(256), nullable=False)
    organization_name = Column(String(256), nullable=False)
    min_salary = Column(Float, nullable=False)
    max_salary = Column(Float, nullable=False)
    salary_interval = Column(String(20), nullable=False)
    who_may_apply = Column(String(63))


class DataEngineer(Base):
    __tablename__ = "data_engineer"

    def __init__(self, table_name: str, *args: Any, **kwargs: Any) -> None:
        __tablename__ = table_name
        super().__init__(*args, **kwargs)

    id = Column(Integer, primary_key=True, nullable=False)
    position_id = Column(String(256), unique=True, nullable=False)
    position_title = Column(String(256), nullable=False)
    organization_name = Column(String(256), nullable=False)
    min_salary = Column(Float, nullable=False)
    max_salary = Column(Float, nullable=False)
    salary_interval = Column(String(20), nullable=False)
    who_may_apply = Column(String(63))


class Data(Base):
    __tablename__ = "data"

    def __init__(self, table_name: str, *args: Any, **kwargs: Any) -> None:
        __tablename__ = table_name
        super().__init__(*args, **kwargs)

    id = Column(Integer, primary_key=True, nullable=False)
    position_id = Column(String(256), unique=True, nullable=False)
    position_title = Column(String(256), nullable=False)
    organization_name = Column(String(256), nullable=False)
    min_salary = Column(Float, nullable=False)
    max_salary = Column(Float, nullable=False)
    salary_interval = Column(String(20), nullable=False)
    who_may_apply = Column(String(63))


class analysis(Base):
    __tablename__ = "analysis"

    def __init__(self, table_name: str, *args: Any, **kwargs: Any) -> None:
        __tablename__ = table_name
        super().__init__(*args, **kwargs)

    id = Column(Integer, primary_key=True, nullable=False)
    position_id = Column(String(256), unique=True, nullable=False)
    position_title = Column(String(256), nullable=False)
    organization_name = Column(String(256), nullable=False)
    min_salary = Column(Float, nullable=False)
    max_salary = Column(Float, nullable=False)
    salary_interval = Column(String(20), nullable=False)
    who_may_apply = Column(String(63))


class Analytics(Base):
    __tablename__ = "analytics"

    def __init__(self, table_name: str, *args: Any, **kwargs: Any) -> None:
        __tablename__ = table_name
        super().__init__(*args, **kwargs)

    id = Column(Integer, primary_key=True, nullable=False)
    position_id = Column(String(256), unique=True, nullable=False)
    position_title = Column(String(256), nullable=False)
    organization_name = Column(String(256), nullable=False)
    min_salary = Column(Float, nullable=False)
    max_salary = Column(Float, nullable=False)
    salary_interval = Column(String(20), nullable=False)
    who_may_apply = Column(String(63))
