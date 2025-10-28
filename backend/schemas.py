from pydantic import BaseModel


"""
PatientCreate
C’est un modèle d’entrée : il définit ce qu’un utilisateur doit envoyer pour créer un patient.
FastAPI va automatiquement :
vérifier les types (int, float, str, etc.),
refuser une requête si un champ est manquant ou invalide.
"""
class PatientCreate(BaseModel):
     age: int
     gender: str
     status: str
     pressurehight: int
     pressurelow: int
     glucose:int
     kcm:float
     troponin:float
     impluse:int
"""
C’est un modèle de sortie : ce que l’API renvoie après avoir créé ou lu un patient.
Il hérite de PatientCreate → donc tous les champs sont inclus, plus id (généré par la base de données).
"""
class PatientResponse(PatientCreate):
     id:int