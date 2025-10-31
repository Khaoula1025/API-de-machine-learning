from fastapi import FastAPI, Depends
from schemas import PatientCreate, PatientResponse
from sqlalchemy.orm import Session
from config import SessionLocal, engine
from models import Base, Patient
import joblib
import pandas as pd
# Créer les tables dans la DB au lancement
Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dépendance pour la session DB
def get_db():
    db = SessionLocal() #Ouvre une nouvelle session
    return db


# Endpoint de prédiction 
@app.post("/predict")
def predict(patient: PatientCreate , db:Session=Depends(get_db)):
    model = joblib.load("cardio_model.pkl")
    # if not model :
    #     raise HTTPException(status_code=503, detail="Modèle non disponible")
    df = pd.DataFrame([patient.__dict__]) # The API transforms this JSON → DataFrame → Model input
    prediction = model.predict(df)[0] # the model outputs either "positive" or "negative"
    message = (
        "Risque cardiovasculaire détecté"
        if prediction == "positive"
        else " Aucun risque détecté"
    )
    return {"prediction": int(prediction), "message": message}

# definir les routes 
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

