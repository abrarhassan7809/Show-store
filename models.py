from sqlalchemy import Column, Integer, ForeignKey, String, TIMESTAMP, Float
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=False, nullable=False)
    designation = Column(String, nullable=False)
    doj = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    age = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    experience = Column(String, nullable=False)
    proof_id = Column(String, nullable=False)
    email = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    address = Column(String, nullable=False)
    month = Column(String, nullable=False)
    year = Column(String, nullable=False)
    basic_salary = Column(String, nullable=False)
    total_days = Column(String, nullable=False)
    absent_days = Column(String, nullable=False)
    medical = Column(String, nullable=False)
    provident_pound = Column(String, nullable=False)
    convince = Column(String, nullable=False)
    net_salary = Column(String, nullable=False)
