from fastapi import FastAPI

from database import Base, engine
from routers import autores, emprestimos, livros, usuarios

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Biblioteca")

app.include_router(usuarios.router)
app.include_router(autores.router)
app.include_router(livros.router)
app.include_router(emprestimos.router)


@app.get("/")
def root():
    return {"message": "API da Biblioteca no ar!"}
