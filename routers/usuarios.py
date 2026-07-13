from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/", response_model=schemas.UsuarioResponse)
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    """Cadastro de usuário (username, email, password). A senha é salva com hash."""
    if crud.get_usuario_by_username(db, usuario.username):
        raise HTTPException(status_code=400, detail="Username já cadastrado")
    if crud.get_usuario_by_email(db, usuario.email):
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.create_usuario(db, usuario)


@router.get("/", response_model=list[schemas.UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.get_usuarios(db)


@router.get("/{usuario_id}", response_model=schemas.UsuarioResponse)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario


@router.put("/{usuario_id}", response_model=schemas.UsuarioResponse)
def atualizar_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.update_usuario(db, usuario_id, usuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario


@router.delete("/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.delete_usuario(db, usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"detail": "Usuário removido com sucesso"}


@router.post("/login")
def login(dados: schemas.LoginRequest, db: Session = Depends(get_db)):
    """Login: recebe username e password e verifica contra o hash salvo."""
    db_usuario = crud.get_usuario_by_username(db, dados.username)
    if not db_usuario or not crud.verify_password(dados.password, db_usuario.password_hash):
        raise HTTPException(status_code=401, detail="Username ou password incorretos")
    return {"detail": "Login realizado com sucesso", "usuario": db_usuario.username}
