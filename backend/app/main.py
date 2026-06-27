from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routes import categorias, produtos, vendas

app = FastAPI(title="BarStock API")

Base.metadata.create_all(bind=engine)

app.include_router(categorias.router)
app.include_router(produtos.router)
app.include_router(vendas.router)

@app.get("/")
def home():
    return {"mensagem": "BarStock API funcionando com PostgreSQL!"}