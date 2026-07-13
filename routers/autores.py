from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post("/", response_model=schemas.AutorResponse)
def criar_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    return crud.create_autor(db, autor)


@router.get("/", response_model=list[schemas.AutorResponse])
def listar_autores(db: Session = Depends(get_db)):
    return crud.get_autores(db)


@router.get("/{autor_id}", response_model=schemas.AutorResponse)
def obter_autor(autor_id: int, db: Session = Depends(get_db)):
    db_autor = crud.get_autor(db, autor_id)
    if not db_autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return db_autor


@router.put("/{autor_id}", response_model=schemas.AutorResponse)
def atualizar_autor(autor_id: int, autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    db_autor = crud.update_autor(db, autor_id, autor)
    if not db_autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return db_autor


@router.delete("/{autor_id}")
def deletar_autor(autor_id: int, db: Session = Depends(get_db)):
    db_autor = crud.delete_autor(db, autor_id)
    if not db_autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return {"detail": "Autor removido com sucesso"}
