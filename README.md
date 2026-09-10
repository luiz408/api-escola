# API Escola

API REST para gerenciamento de estudantes, cursos e matrículas, construída com Django e Django REST Framework.

## Recursos

- CRUD de estudantes e cursos.
- Criação e consulta de matrículas.
- Consulta de matrículas por estudante ou curso.
- Pesquisa de estudantes por nome ou CPF.
- Ordenação de estudantes por nome.
- Documentação interativa com Swagger e ReDoc.
- Versionamento de estudantes por parâmetro de consulta (`v1` e `v2`).

## Requisitos

- Python 3.12 ou superior
- Docker e Docker Compose (opcional)

## Execução local

No Windows, crie e ative um ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instale as dependências e execute as migrações:

```powershell
pip install -r requeriments.txt
python manage.py migrate
python manage.py runserver
```

A API ficará disponível em `http://127.0.0.1:8000/`.

## Execução com Docker

```powershell
docker compose up --build
```

A aplicação ficará disponível em `http://localhost:8000/`.

## Endpoints principais

| Método                  | Endpoint                       | Descrição                       |
| ----------------------- | ------------------------------ | ------------------------------- |
| GET, POST               | `/estudantes/`                 | Lista ou cadastra estudantes    |
| GET, PUT, PATCH, DELETE | `/estudantes/{id}/`            | Consulta ou altera um estudante |
| GET, POST               | `/cursos/`                     | Lista ou cadastra cursos        |
| GET, PUT, PATCH, DELETE | `/cursos/{id}/`                | Consulta ou altera um curso     |
| GET, POST               | `/matriculas/`                 | Lista ou cadastra matrículas    |
| GET                     | `/estudantes/{id}/matriculas/` | Lista matrículas do estudante   |
| GET                     | `/cursos/{id}/matriculas/`     | Lista matrículas do curso       |

Para usar a versão 2 do serializer de estudantes, utilize `?version=v2`:

```text
/estudantes/?version=v2
```

## Documentação

- Swagger: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Git

O arquivo `.gitignore` exclui configurações locais (`.env`), o ambiente virtual, o banco SQLite e arquivos gerados pelo Python.
