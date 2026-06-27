# 🍺 BarStock

Sistema de gerenciamento de estoque para bares desenvolvido como projeto final da disciplina **C216 – Engenharia de Software**.

O projeto utiliza uma arquitetura separada entre **Backend** e **Frontend**, com banco de dados PostgreSQL e execução através de Docker Compose.

---

## 📌 Tecnologias Utilizadas

### Backend
- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn

### Frontend
- Flask
- HTML5
- CSS3

### Infraestrutura
- Docker
- Docker Compose

---

# 📂 Estrutura do Projeto

```
Projeto-final-C216
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── crud.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── __init__.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── tests/
│
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Arquitetura

```
          Frontend (Flask)
                 │
                 │ HTTP
                 ▼
         Backend (FastAPI)
                 │
                 │ SQLAlchemy
                 ▼
          PostgreSQL
```

---

# 🚀 Como executar

## 1. Clonar o repositório

```bash
git clone https://github.com/bissacot/Projeto-final-C216.git
```

Entre na pasta:

```bash
cd Projeto-final-C216
```

---

## 2. Executar com Docker

```bash
docker compose up --build
```

---

## 3. Backend

Após iniciar os containers, acesse:

```
http://localhost:8000
```

Resposta esperada:

```json
{
  "mensagem": "BarStock API funcionando com PostgreSQL!"
}
```

---

## 4. Documentação da API

O FastAPI disponibiliza automaticamente a documentação:

```
http://localhost:8000/docs
```

---

# 📦 Funcionalidades

Atualmente o projeto possui:

- Estrutura separada entre Backend e Frontend
- API desenvolvida com FastAPI
- Integração com PostgreSQL
- Containerização utilizando Docker
- Organização em camadas

---

# 🚧 Em desenvolvimento

As seguintes funcionalidades ainda estão em implementação:

- Cadastro de Produtos
- Cadastro de Categorias
- Registro de Vendas
- Interface Web completa
- Operações CRUD
- Modelos do banco de dados
- Validação com Pydantic
- Testes automatizados

---

# 📁 Organização do Backend

O backend foi estruturado seguindo o padrão recomendado pelo FastAPI.

| Arquivo | Responsabilidade |
|----------|------------------|
| main.py | Inicialização da API |
| database.py | Configuração do banco |
| routes/ | Endpoints |
| models.py | Modelos SQLAlchemy |
| schemas.py | Schemas Pydantic |
| crud.py | Operações de banco |

---

# 🐳 Docker

A aplicação utiliza Docker Compose para inicializar os serviços:

- Backend
- PostgreSQL

Basta executar:

```bash
docker compose up --build
```

---

# 📖 Disciplina

Projeto desenvolvido para a disciplina:

**C216 – Engenharia de Software**

Instituto Nacional de Telecomunicações – INATEL

---

# 👨‍💻 Autor

**Gabriel Bissacot Fraguas**

GitHub:

https://github.com/bissacot