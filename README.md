# API Biblioteca

API REST simples (FastAPI + SQLAlchemy) para controle de uma biblioteca: usuários, autores, livros e empréstimos.

## Setup rápido

1. `uv sync` — instala as dependências
2. Crie o banco `biblioteca` no PostgreSQL (via DBeaver)
3. Edite `database.py` com o usuário/senha do seu Postgres
4. `uv run uvicorn main:app --reload`
5. Acesse http://127.0.0.1:8000/docs

## Estrutura

- `database.py` — conexão com o banco
- `models.py` — classes do ORM (tabelas)
- `schemas.py` — validação de entrada/saída (Pydantic)
- `crud.py` — funções que mexem no banco
- `routers/` — rotas da API (GET, POST, PUT, DELETE)
- `main.py` — junta tudo e sobe a aplicação
