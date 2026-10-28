# 📘 Atividade: Testes Automatizados para APIs com pytest

## 🎯 Objetivo

Escreva testes automatizados para verificar o comportamento de uma API REST criada com FastAPI. Você praticará assertions, o `TestClient` e o isolamento do estado entre testes.

## 📝 Tarefas

### 🛠️ Testar as rotas de consulta

#### Descrição
Complete os testes para listar os livros, consultar um livro existente e verificar a resposta para um ID inexistente. Antes de começar, conclua a atividade Building REST APIs com FastAPI.

#### Requisitos
Os testes devem:

- Verificar que `GET /books` retorna status `200` e os livros esperados.
- Verificar que `GET /books/1` retorna status `200` e os dados do livro com ID `1`.
- Verificar que a consulta a um ID inexistente retorna status `404`.

### 🛠️ Testar a criação de livros

#### Descrição
Escreva um teste para enviar um novo livro à API e conferir a resposta e a alteração no catálogo.

#### Requisitos
Os testes devem:

- Enviar título e autor para `POST /books`.
- Verificar o status `201` e os dados do livro criado, incluindo o ID.
- Confirmar que o livro criado aparece em uma consulta a `GET /books`.

### 🛠️ Testar atualização e remoção

#### Descrição
Complete os testes para atualizar e remover livros e para tratar IDs inexistentes nessas operações.

#### Requisitos
Os testes devem:

- Verificar que `PUT /books/1` atualiza o título e o autor e retorna status `200`.
- Verificar que `DELETE /books/1` retorna status `204` e remove o livro do catálogo.
- Verificar que `PUT` e `DELETE` para um ID inexistente retornam status `404`.

Para executar os testes, instale as dependências com `python -m pip install fastapi uvicorn pytest httpx` e rode `pytest starter-code.py -v` dentro desta pasta.