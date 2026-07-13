import bcrypt
from sqlalchemy.orm import Session

import models
import schemas


# ---------------- Senha ----------------
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))


# ---------------- Usuario ----------------
def get_usuarios(db: Session):
    return db.query(models.Usuario).all()


def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()


def get_usuario_by_username(db: Session, username: str):
    return db.query(models.Usuario).filter(models.Usuario.username == username).first()


def get_usuario_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()


def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(
        username=usuario.username,
        email=usuario.email,
        password_hash=hash_password(usuario.password),
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db_usuario.username = usuario.username
        db_usuario.email = usuario.email
        db_usuario.password_hash = hash_password(usuario.password)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario


def delete_usuario(db: Session, usuario_id: int):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario


# ---------------- Autor ----------------
def get_autores(db: Session):
    return db.query(models.Autor).all()


def get_autor(db: Session, autor_id: int):
    return db.query(models.Autor).filter(models.Autor.id == autor_id).first()


def create_autor(db: Session, autor: schemas.AutorCreate):
    db_autor = models.Autor(**autor.model_dump())
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor


def update_autor(db: Session, autor_id: int, autor: schemas.AutorCreate):
    db_autor = get_autor(db, autor_id)
    if db_autor:
        db_autor.nome = autor.nome
        db_autor.nacionalidade = autor.nacionalidade
        db.commit()
        db.refresh(db_autor)
    return db_autor


def delete_autor(db: Session, autor_id: int):
    db_autor = get_autor(db, autor_id)
    if db_autor:
        db.delete(db_autor)
        db.commit()
    return db_autor


# ---------------- Livro ----------------
def get_livros(db: Session):
    return db.query(models.Livro).all()


def get_livro(db: Session, livro_id: int):
    return db.query(models.Livro).filter(models.Livro.id == livro_id).first()


def create_livro(db: Session, livro: schemas.LivroCreate):
    db_livro = models.Livro(**livro.model_dump())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro


def update_livro(db: Session, livro_id: int, livro: schemas.LivroCreate):
    db_livro = get_livro(db, livro_id)
    if db_livro:
        db_livro.titulo = livro.titulo
        db_livro.isbn = livro.isbn
        db_livro.ano_publicacao = livro.ano_publicacao
        db_livro.autor_id = livro.autor_id
        db.commit()
        db.refresh(db_livro)
    return db_livro


def delete_livro(db: Session, livro_id: int):
    db_livro = get_livro(db, livro_id)
    if db_livro:
        db.delete(db_livro)
        db.commit()
    return db_livro


# ---------------- Emprestimo ----------------
def get_emprestimos(db: Session):
    return db.query(models.Emprestimo).all()


def get_emprestimo(db: Session, emprestimo_id: int):
    return db.query(models.Emprestimo).filter(models.Emprestimo.id == emprestimo_id).first()


def create_emprestimo(db: Session, emprestimo: schemas.EmprestimoCreate):
    db_emprestimo = models.Emprestimo(**emprestimo.model_dump())
    db.add(db_emprestimo)
    db.commit()
    db.refresh(db_emprestimo)
    return db_emprestimo


def update_emprestimo(db: Session, emprestimo_id: int, emprestimo: schemas.EmprestimoCreate):
    db_emprestimo = get_emprestimo(db, emprestimo_id)
    if db_emprestimo:
        db_emprestimo.usuario_id = emprestimo.usuario_id
        db_emprestimo.livro_id = emprestimo.livro_id
        db_emprestimo.data_emprestimo = emprestimo.data_emprestimo
        db_emprestimo.data_devolucao = emprestimo.data_devolucao
        db_emprestimo.devolvido = emprestimo.devolvido
        db.commit()
        db.refresh(db_emprestimo)
    return db_emprestimo


def delete_emprestimo(db: Session, emprestimo_id: int):
    db_emprestimo = get_emprestimo(db, emprestimo_id)
    if db_emprestimo:
        db.delete(db_emprestimo)
        db.commit()
    return db_emprestimo
