from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(prefix="/livros", tags=["Livros"])


@router.post("/", response_model=schemas.LivroResponse)
def criar_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    if not crud.get_autor(db, livro.autor_id):
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return crud.create_livro(db, livro)


@router.get("/", response_model=list[schemas.LivroResponse])
def listar_livros(db: Session = Depends(get_db)):
    return crud.get_livros(db)


@router.get("/{livro_id}", response_model=schemas.LivroResponse)
def obter_livro(livro_id: int, db: Session = Depends(get_db)):
    db_livro = crud.get_livro(db, livro_id)
    if not db_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_livro


@router.put("/{livro_id}", response_model=schemas.LivroResponse)
def atualizar_livro(livro_id: int, livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    if not crud.get_autor(db, livro.autor_id):
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    db_livro = crud.update_livro(db, livro_id, livro)
    if not db_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_livro


@router.delete("/{livro_id}")
def deletar_livro(livro_id: int, db: Session = Depends(get_db)):
    db_livro = crud.delete_livro(db, livro_id)
    if not db_livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return {"detail": "Livro removido com sucesso"}
