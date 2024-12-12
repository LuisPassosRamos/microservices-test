# Criando e Testando Dois Microsserviços

## Objetivo
1. Criar dois microsserviços independentes:
   - **Serviço de API (App)**: Responsável por gerenciar usuários.
   - **Serviço de "banco de dados"**: Responsável por armazenar usuários.
2. Integrar os serviços e testar a integração usando ferramentas como **Postman** ou **Swagger**.

---

## Requisitos

### 1. Linguagem de Programação
- Python, Java, ou outra linguagem de sua preferência.

### 2. Banco de Dados
- Utilizar **Firebird** ou simular o armazenamento usando um arquivo **JSON**.

### 3. API RESTful
- Criar dois endpoints:
  - **GET /users**: Retorna uma lista de usuários.
  - **POST /users**: Adiciona um novo usuário ao banco.

### 4. Testes
- Rodar os microsserviços localmente.
- Testar os endpoints utilizando **Postman** ou **Swagger**.

---

## Instruções Gerais
1. Garanta que os microsserviços estejam configurados para se comunicar corretamente.
2. Documente a API para facilitar os testes e uso posterior.
3. Certifique-se de tratar erros e retornar respostas apropriadas nos endpoints.
