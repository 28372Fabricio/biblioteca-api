from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Usuario(Base):
    """Usuário do sistema (cadastro + login)."""
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    emprestimos = relationship("Emprestimo", back_populates="usuario")


class Autor(Base):
    """Autor de livros."""
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    nacionalidade = Column(String(50), nullable=True)

    livros = relationship("Livro", back_populates="autor")


class Livro(Base):
    """Livro do acervo. Ligado a um Autor (N:1)."""
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    isbn = Column(String(20), nullable=True)
    ano_publicacao = Column(Integer, nullable=True)
    autor_id = Column(Integer, ForeignKey("autores.id"), nullable=False)

    autor = relationship("Autor", back_populates="livros")
    emprestimos = relationship("Emprestimo", back_populates="livro")


class Emprestimo(Base):
    """Empréstimo de um Livro para um Usuario. Ligado a Usuario (N:1) e Livro (N:1)."""
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=True)
    devolvido = Column(Boolean, default=False)

    usuario = relationship("Usuario", back_populates="emprestimos")
    livro = relationship("Livro", back_populates="emprestimos")
