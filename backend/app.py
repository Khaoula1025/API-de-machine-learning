from fastapi import FastAPI, Depends
from schemas import PatientCreate, PatientResponse
from sqlalchemy.orm import Session
from config import SessionLocal, engine
from models import Base, Patient
import joblib
import pandas as pd
# Crée dans la base de données toutes les tables définies dans mes modèles SQLAlchemy (dans models.py) si elles n’existent pas encore.”
Base.metadata.create_all(bind=engine)
# Initialiser l'application FastAPI
app = FastAPI() 

# Dépendance pour la session DB
"""
Chaque fois qu’un utilisateur fait une requête à ton API :
FastAPI appellera get_db()
Cela crée une nouvelle connexion à ta base de données
Puis ton route reçoit cette session dans db: Session = Depends(get_db)
"""
def get_db():
    db = SessionLocal() #Ouvre une nouvelle session
    return db


# Route de prédiction avec le modèle ML
"""
Ce qui se passe :
Tu envoies un JSON de patient (âge, pression, glucose, etc.)
L’API transforme ce JSON en objet PatientCreate (validation automatique).
pandas le convertit en DataFrame (format accepté par ton modèle ML).
Le modèle prédictif (chargé avec joblib) fait une prédiction :
1 = Risque détecté
0 = Aucun risque
"""


@app.post("/predict")
def predict(patient: PatientCreate , db:Session=Depends(get_db)):
    model = joblib.load("cardio_model.pkl")
    df = pd.DataFrame([patient.__dict__]) # The API transforms this JSON → patient.__dict__ transforme ton objet Python en dictionnaire puis pandas le transforme en DataFrame → Model input
    prediction = model.predict(df)[0] # the model outputs either "positive" or "negative"
    message = (
        "Risque cardiovasculaire détecté"
        if prediction == 1
        else " Aucun risque détecté"
    )
    return {"prediction": int(prediction), "message": message}

# definir les routes 
@app.get("/")
def home():
    return{"message":"Bonjour"}


# Route pour lister les patients
@app.get("/patients",response_model=list[PatientResponse]) #response_model=list[PatientResponse] → parametre ndemno la réponse sera proprement formatée selon le schéma
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all() # une liste d’objets SQLAlchemy/query ncpesiw model:la table lli bghit njib mnha les patients

#Route pour ajouter un nouveau patient
"""
Reçoit un JSON de patient
Crée un objet Patient pour la base de données
L’enregistre dans la table (db.add, db.commit)
Retourne le patient ajouté (avec son id généré automatiquement)
"""
@app.post("/patients",response_model=PatientResponse) #response_model=PatientResponse → la réponse sera formatée selon le schéma PatientResponse
def create_patient(patient:PatientCreate, db: Session = Depends(get_db)):
    new_patient = Patient(**patient.dict()) #Crée un objet Patient avec toutes les données reçues automatiquement
    db.add(new_patient) #Prépare l'ajout dans la DB/Ajoute le patient à la session (en attente d’être sauvegardé)
    db.commit() #Valide l'ajout dans la DB
    db.refresh(new_patient) #Récupère les données mises à jour (comme l'id généré par la DB)
    return new_patient #Return le patient créé

