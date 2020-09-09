from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
from pydantic import BaseModel, constr
from typing import List
from sqlalchemy import Column, Integer, String, Float
from utils.database import Base


class TestTable(Base):
    __tablename__='TestTable'
    parameter_set = Column(Integer, primary_key=True, nullable=False)
    likelihood = Column(Float,unique=False)
    horizontal_flux_total =Column(Float,unique=False)
    vertical_flux = Column(Float,unique=False)
    PM1 = Column(Float,unique=False)
    PM2_5 = Column(Float,unique=False)
    PM10 = Column(Float,unique=False)
