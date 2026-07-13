from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(prefix="/emprestimos", tags=["Empréstimos"])


@router.post("/", response_model=schemas.EmprestimoResponse)
def criar_emprestimo(emprestimo: schemas.EmprestimoCreate, db: Session = Depends(get_db)):
    if not crud.get_usuario(db, emprestimo.usuario_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    if not crud.get_livro(db, emprestimo.livro_id):
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return crud.create_emprestimo(db, emprestimo)


@router.get("/", response_model=list[schemas.EmprestimoResponse])
def listar_emprestimos(db: Session = Depends(get_db)):
    return crud.get_emprestimos(db)


@router.get("/{emprestimo_id}", response_model=schemas.EmprestimoResponse)
def obter_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    db_emprestimo = crud.get_emprestimo(db, emprestimo_id)
    if not db_emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return db_emprestimo


@router.put("/{emprestimo_id}", response_model=schemas.EmprestimoResponse)
def atualizar_emprestimo(emprestimo_id: int, emprestimo: schemas.EmprestimoCreate, db: Session = Depends(get_db)):
    db_emprestimo = crud.update_emprestimo(db, emprestimo_id, emprestimo)
    if not db_emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return db_emprestimo


@router.delete("/{emprestimo_id}")
def deletar_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    db_emprestimo = crud.delete_emprestimo(db, emprestimo_id)
    if not db_emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return {"detail": "Empréstimo removido com sucesso"}
