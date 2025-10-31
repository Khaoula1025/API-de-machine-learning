from sqlalchemy import Column, Integer, String, Float
from config import Base

class Patient(Base):
    __tablename__ ="patients" # nom de la table dans la DB / 

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(Integer)
    status = Column(String)
    pressurehight = Column(Integer)
    pressurelow = Column(Integer)
    glucose = Column(Integer)
    kcm = Column(Float)
    troponin = Column(Float)
    impluse = Column(Integer)
