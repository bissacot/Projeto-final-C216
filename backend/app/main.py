from fastapi import FastAPI

from app.database import Base, engine

app = FastAPI(title="BarStock API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"mensagem": "BarStock API funcionando com PostgreSQL!"}