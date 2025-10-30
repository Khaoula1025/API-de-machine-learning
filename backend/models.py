from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Base
from config import Base
# engine = create_engine('sqlite:///./patients.csv"')

class Patient(Base):
    __tablename__ ="patients"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(String)
    status = Column(String)
    pressurehight = Column(Integer)
    pressurelow = Column(Integer)
    glucose = Column(Integer)
    kcm = Column(Float)
    troponin = Column(Float)
    impluse = Column(Integer)
