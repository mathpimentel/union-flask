# API de Tarefas com Flask

Este projeto é uma API REST simples feita com Flask para cadastrar, listar, atualizar e remover tarefas. A aplicação usa uma lista em memória como armazenamento, ou seja, os dados são reiniciados sempre que o servidor é reiniciado.

## Funcionalidades

- Listar todas as tarefas cadastradas
- Buscar uma tarefa pelo ID
- Criar uma nova tarefa
- Atualizar uma tarefa existente
- Excluir uma tarefa

## Tecnologias utilizadas

- Python
- Flask
- Werkzeug
- Flask-SQLAlchemy
- Flask-Cors

> Observação: no estado atual do projeto, as tarefas ficam salvas apenas em memória. As dependências `Flask-SQLAlchemy` e `Flask-Cors` estão no `requirements.txt`, mas ainda não são usadas diretamente no código principal.

## Estrutura do projeto

```text
union-flask/
|-- app.py
|-- requirements.txt
|-- models/
|   `-- task.py
`-- README.md
```

## Como executar o projeto

### 1. Criar um ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
```

### 2. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 4. Executar a aplicação

```powershell
python app.py
```

Por padrão, a API será iniciada em:

```text
http://127.0.0.1:8000
```

## Rotas da API

### Listar todas as tarefas

```http
GET /tasks
```

Exemplo:

```powershell
curl http://127.0.0.1:8000/tasks
```

Resposta esperada:

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Estudar Flask",
      "description": "Aprender os conceitos básicos do Flask.",
      "completed": false
    }
  ],
  "total_tasks": 5
}
```

### Buscar uma tarefa pelo ID

```http
GET /tasks/<id>
```

Exemplo:

```powershell
curl http://127.0.0.1:8000/tasks/1
```

Caso o ID não exista, a API retorna status `404`.

### Criar uma tarefa

```http
POST /tasks
```

Exemplo:

```powershell
curl -X POST http://127.0.0.1:8000/tasks `
  -H "Content-Type: application/json" `
  -d "{\"title\":\"Nova tarefa\",\"description\":\"Descrição da nova tarefa\"}"
```

Campos aceitos:

- `title`: título da tarefa
- `description`: descrição da tarefa

Se `description` não for enviada, a API usa o valor padrão `"..."`.

### Atualizar uma tarefa

```http
PUT /tasks/<id>
```

Exemplo:

```powershell
curl -X PUT http://127.0.0.1:8000/tasks/1 `
  -H "Content-Type: application/json" `
  -d "{\"title\":\"Estudar Flask\",\"description\":\"Revisar rotas e JSON\",\"completed\":true}"
```

Campos esperados:

- `title`
- `description`
- `completed`

Caso o ID não exista, a API retorna status `404`.

### Excluir uma tarefa

```http
DELETE /tasks/<id>
```

Exemplo:

```powershell
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

Caso o ID não exista, a API retorna status `404`.

## Modelo de tarefa

Cada tarefa possui a seguinte estrutura:

```json
{
  "id": 1,
  "title": "Título da tarefa",
  "description": "Descrição da tarefa",
  "completed": false
}
```

## Observações importantes

- O servidor roda em modo debug.
- A porta configurada no projeto é `8000`.
- Não existe banco de dados configurado no código atual.
- As tarefas iniciais ficam definidas diretamente em `app.py`.
