from fastapi import FastAPI
from app.routers.product_router import router

app = FastAPI(
    title="API de Produtos",
    description="API simples para CRUD de produtos usando FastAPI, SQLAlchemy e SQLite",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "API funcionando!"}
