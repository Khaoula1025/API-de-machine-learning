from fastapi import FastAPI, Depends
from schemas import PatientCreate, PatientResponse
from sqlalchemy.orm import Session
from config import SessionLocal, engine
from models import Base, Patient
# Créer les tables dans la DB au lancement
Base.metadata.create_all(bind=engine)
app = FastAPI()
# Dépendance pour la session DB
def get_db():
    db = SessionLocal() #Ouvre une nouvelle session
    try:
        yield db 
    finally:
        db.close() 

@app.get("/")
def home():
    return{"message":"Bonjour"}

@app.get("/patients",response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

@app.post("/patients",response_model=PatientResponse)
def create_patient(patient:PatientCreate, db: Session = Depends(get_db)):
    new_patient = Patient(**patient.dict()) #Crée un objet Patient avec toutes les données reçues automatiquement
    db.add(new_patient) #Prépare l'ajout dans la DB/Ajoute le patient à la session (en attente d’être sauvegardé)
    db.commit() #Valide l'ajout dans la DB
    db.refresh(new_patient) #Récupère les données mises à jour (comme l'id généré par la DB)
    return new_patient #Return le patient créé



# @app.get("/patients")
# def get_patients():
#     return read_patients()
