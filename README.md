# 🫀 API de Prédiction du Risque Cardiovasculaire

## 📘 Contexte du Projet

Les **maladies cardiovasculaires** sont la première cause de mortalité dans le monde, responsables de plus de **17,9 millions de décès par an**.
Ce projet vise à développer une **API prédictive** capable d’estimer le risque qu’un patient développe une maladie cardiaque, à partir de ses données cliniques.

L’objectif final est de fournir une API simple et efficace qui :

* Enregistre les informations d’un patient dans une base de données.
* Retourne un **score de risque cardiovasculaire** à l’aide d’un modèle de Machine Learning.

---

## 👥 Travail en Binôme

### Rôles et Responsabilités

* **Développeur Backend :**

  * Création de la structure FastAPI.
  * Intégration de la base de données SQLite avec SQLAlchemy.
  * Développement des routes `POST /patients` et `GET /patients`.

* **Développeur IA / Data :**

  * Nettoyage et préparation du dataset.
  * Entraînement et sauvegarde du modèle de Machine Learning.
  * Intégration du modèle dans la route `/predict_risk`.

### Collaboration GitHub

* Une branche `main`.
* Deux branches de fonctionnalités :

  * `feature/api`
  * `feature/ml`

---

## ⚙️ Technologies Utilisées

* **Backend :** FastAPI
* **Base de données :** SQLite + SQLAlchemy
* **Validation :** Pydantic
* **Machine Learning :** Scikit-learn
* **Tests :** Pytest + TestClient
* **Documentation :** Swagger (intégré à FastAPI)
* **Gestion de version :** GitHub

---

## 🧱 Structure du Projet

```
📁 API-de-machine-learning
│
├── backend/
│   ├── app.py  
│   ├── cardio_model.pkl        
│   ├── config.py             
│   ├── models.py                
│   |── schemas.py
|   └──test_api.py               
│── ml/
│   ├── eda.ipynb     
│   └── model_training.ipynb   
│
├── data.csv                             
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Lancement

### 1. Cloner le projet

```bash
git clone https://github.com/khaoula1025/API-de-machine-learning.git
cd API-de-machine-learning
```

### 2. Créer un environnement virtuel

```bash
python -m venv env
source env/bin/activate       # macOS / Linux
env\Scripts\activate          # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer le serveur FastAPI

```bash
uvicorn backend.app:app --reload
```

### 5. Accéder à la documentation interactive

Ouvrir dans le navigateur :

```
http://127.0.0.1:8000/docs
```

---

## 📡 Endpoints Principaux

### ➕ POST /patients

Ajoute un nouveau patient à la base de données.
**Exemple de requête :**

```json
{
        "age": 50,
        "gender": 0,
        "pressurehight": 21,
        "pressurelow": 9,
        "glucose":11,
        "kcm":11.8,
        "troponin":5.9,
        "impluse":8
    }
```
---

### 📋 GET /patients

Liste tous les patients enregistrés.
**Réponse :**

```json
[
  {
        "age": 50,
        "gender": 0,
        "pressurehight": 21,
        "pressurelow": 9,
        "glucose":11,
        "kcm":11.8,
        "troponin":5.9,
        "impluse":8
    }
]
```

---

### 🧠 POST /predict

Prend les données d’un patient et retourne si  **le patient risque d'avoir cette maladie ou pas **.

**Exemple de requête :**

```json
{
        "age": 50,
        "gender": 0,
        "pressurehight": 21,
        "pressurelow": 9,
        "glucose":11,
        "kcm":11.8,
        "troponin":5.9,
        "impluse":8
    }
```

**Réponse :**

```json
{
  "prediction": 0,
  "message": " Aucun risque détecté"
}
```

---

## 🧪 Tests Unitaires

### Lancer les tests

```bash
pytest -v
```

### Vérifications principales

* Le statut `200` pour la route `/predict`
* Les données des patients bien enregistrées et listées

---

## 📊 Partie Machine Learning

### Étapes principales :

1. Chargement et nettoyage du dataset.
2. Transformation des variables numériques et catégorielles.
3. Séparation des données : `X` (features) et `y` (cible).
4. Création d’un **pipeline Scikit-learn** (préprocessing + modèle).
5. Entraînement du modèle.
6. Sauvegarde du modèle :

   ```python
   joblib.dump(model, "model.joblib")
   ```
7. (Bonus) Optimisation avec `GridSearchCV`.

---

## 🧾 Modalités Pédagogiques

* **Travail en binôme**
* **Durée :** 5 jours (du 27/10/2025 au 31/10/2025)
* **Livraison :**

  * API fonctionnelle
  * Modèle ML intégré
  * Tests unitaires validés
  * Documentation complète (README + Swagger)

---

## 📦 Livrables

1. Code source complet sur GitHub.
2. Base SQLite contenant les patients.
3. Modèle ML entraîné (`model.joblib`).
4. Tests unitaires (`pytest`).
5. Documentation :

   * `README.md`
   * Swagger `/docs`
6. Lien Jira du projet.

---

## 🏁 Critères de Performance

| Critère           | Description                                           |
| ----------------- | ----------------------------------------------------- |
| ✅ Fonctionnalité  | Routes `/patients` et `/predict_risk` opérationnelles |
| ✅ Précision       | Modèle bien entraîné et intégré                       |
| ✅ Qualité du Code | Structure claire, bien commentée                      |
| ✅ Collaboration   | Branches Git bien gérées et commits cohérents         |
| ✅ Documentation   | README complet + Swagger                              |
| ✅ Tests           | API validée par Pytest                                |

---

## 🧑‍💻 Auteurs

* **Karima Chami** – Développeuse Backend
* **Khaoula Esioudi** – Développeur IA / Data

Projet réalisé dans le cadre du **brief API de Machine Learning** – Simplon Maghreb, 2025.
