from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


# ---------------- Usuario ----------------
class UsuarioBase(BaseModel):
    username: str
    email: str


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioResponse(UsuarioBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    username: str
    password: str


# ---------------- Autor ----------------
class AutorBase(BaseModel):
    nome: str
    nacionalidade: Optional[str] = None


class AutorCreate(AutorBase):
    pass


class AutorResponse(AutorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ---------------- Livro ----------------
class LivroBase(BaseModel):
    titulo: str
    isbn: Optional[str] = None
    ano_publicacao: Optional[int] = None
    autor_id: int


class LivroCreate(LivroBase):
    pass


class LivroResponse(LivroBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# ---------------- Emprestimo ----------------
class EmprestimoBase(BaseModel):
    usuario_id: int
    livro_id: int
    data_emprestimo: date
    data_devolucao: Optional[date] = None
    devolvido: bool = False


class EmprestimoCreate(EmprestimoBase):
    pass


class EmprestimoResponse(EmprestimoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
