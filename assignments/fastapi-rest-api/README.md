# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar um catálogo de livros usando FastAPI. Você praticará rotas, métodos HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Consultar livros pela API

#### Descrição
Complete as rotas de consulta para listar os livros cadastrados e buscar um livro pelo seu ID. Instale as dependências com `python -m pip install fastapi uvicorn`, inicie o servidor com `python starter-code.py` e use `/docs` para testar as rotas.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books` com a lista de livros e status `200`.
- Responder a `GET /books/{book_id}` com o livro correspondente e status `200`.
- Retornar status `404` quando o ID solicitado não existir.

### 🛠️ Cadastrar livros

#### Descrição
Implemente a rota para cadastrar um livro no catálogo usando os dados enviados pelo cliente.

#### Requisitos
O programa concluído deve:

- Aceitar `POST /books` com título e autor no corpo da requisição.
- Usar o modelo Pydantic fornecido para validar os dados recebidos.
- Atribuir um ID ao novo livro e incluí-lo no catálogo.
- Retornar o livro criado com status `201`.

### 🛠️ Atualizar e remover livros

#### Descrição
Implemente as rotas para substituir os dados de um livro existente e removê-lo do catálogo.

#### Requisitos
O programa concluído deve:

- Aceitar `PUT /books/{book_id}` para atualizar o título e o autor do livro.
- Aceitar `DELETE /books/{book_id}` para remover o livro e retornar status `204`.
- Retornar status `404` ao tentar atualizar ou remover um ID inexistente.