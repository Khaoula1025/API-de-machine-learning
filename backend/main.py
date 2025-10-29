from fastapi import FastAPI

app=FastAPI()

#endpoints
@app.get("/")

def root():
    return {"message:Welcome to your introduction to FastApi"}