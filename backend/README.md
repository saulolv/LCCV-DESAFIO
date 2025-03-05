# Sistema Projetos

Sistema de gerenciamento de projetos, financiadores, áreas tecnológicas e colaboradores desenvolvido com Django 3.2 e Django REST Framework.

## Requisitos

- Python 3.9+
- PostgreSQL
- Bibliotecas Python listadas em requirements.txt

## Configuração do Ambiente

### 1. Clone o repositório

```bash
git clone [url-do-repositorio]
cd sistema_projetos
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados PostgreSQL

Crie um banco de dados PostgreSQL:

```sql
CREATE DATABASE sistema_projetos;
CREATE USER sistema_user WITH PASSWORD 'sua_senha';
ALTER ROLE sistema_user SET client_encoding TO 'utf8';
ALTER ROLE sistema_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE sistema_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE sistema_projetos TO sistema_user;
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
DB_NAME=sistema_projetos
DB_USER=sistema_user
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

### 6. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crie um superusuário para acessar o admin

```bash
python manage.py createsuperuser
```

### 8. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

## Acessando o Sistema

- **Interface Admin**: http://localhost:8000/admin/
- **API Documentation**: 
  - Swagger UI: http://localhost:8000/api/swagger/
  - ReDoc: http://localhost:8000/api/redoc/
  - Schema (JSON): http://localhost:8000/api/schema/

## Endpoints da API

### Projetos
- `GET /api/projetos/form/` - Dados para formulário de projetos
- `GET /api/projetos/listar/` - Listar todos os projetos
- `POST /api/projetos/cadastrar/` - Cadastrar um novo projeto
- `POST /api/projetos/{id}/inativar/` - Inativar um projeto
- `PATCH /api/projetos/{id}/editar/` - Editar um projeto
- `GET /api/projetos/{id}/visualizar/` - Visualizar detalhes de um projeto
- `GET /api/projetos/{id}/equipe/` - Visualizar equipe de um projeto
- `PATCH /api/projetos/{id}/equipe/atualizar/` - Atualizar equipe de um projeto

### Colaboradores
- `GET /api/colaboradores/listar/` - Listar todos os colaboradores
- `POST /api/colaboradores/cadastrar/` - Cadastrar um novo colaborador
- `GET /api/colaboradores/{id}/visualizar/` - Visualizar detalhes de um colaborador
- `PATCH /api/colaboradores/{id}/editar/` - Editar um colaborador

### Financiadores e Áreas Tecnológicas
- Endpoints padrão REST também disponíveis para Financiadores e Áreas Tecnológicas