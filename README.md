# SGE - Sistema de Gestão de Estoque (Full-Stack)

![Status](https://img.shields.io/badge/Status-Concluído%20(v1.0)-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.x-darkgreen?logo=django)
![Django REST](https://img.shields.io/badge/Django%20REST-Framework-red?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-purple?logo=bootstrap)

> Um sistema web full-stack completo para gerenciamento de estoque, construído com Python, Django, Django Rest Framework e Bootstrap 5. O projeto inclui um frontend administrativo e uma API RESTful segura pronta para integrações.

---

## ✨ Funcionalidades Principais

Este projeto não é apenas um frontend, mas uma plataforma de gestão completa com lógica de negócios robusta.

* **Dashboard Analítico:** Tela inicial com métricas vitais em tempo real (Custo de estoque, Valor total, Lucro, Gráficos de vendas, etc.).
* **Autenticação Segura:** Sistema de login para o frontend e autenticação baseada em Token (JWT) para a API.
* **Gestão Completa (CRUD):** Módulos para gerenciar:
    * Produtos
    * Fornecedores
    * Categorias
    * Marcas
* **Controle de Fluxo de Estoque:**
    * **Entradas (Inflows):** Registro de compra de produtos, atualizando o estoque e o custo.
    * **Saídas (Outflows):** Registro de vendas, abatendo o estoque e calculando o lucro.
* **Painel de Administração (Django Admin):** Acesso de superusuário para gerenciamento de baixo nível de usuários, permissões e modelos de dados.
* **API RESTful Completa:** Todos os módulos são expostos via uma API segura, permitindo integrações futuras.

---

## 🏛️ Arquitetura e API RESTful

O SGE foi construído com uma arquitetura desacoplada em mente. O backend Django serve tanto o frontend (renderizado no servidor com Bootstrap 5) quanto a API RESTful (usando Django Rest Framework).

### Destaques da API:

* **Autenticação JWT:** A API é protegida usando `djangorestframework-simplejwt`. O acesso requer um *access token* válido, obtido via endpoint de login.
* **Permissões:** A API respeita as permissões de usuário do Django, garantindo que um usuário só possa ver ou modificar dados que lhe são permitidos.
* **Escalabilidade:** A existência desta API torna trivial a criação de novas aplicações (ex: um **aplicativo mobile** em React Native ou Flutter) que consumam os mesmos dados, sem precisar reescrever a lógica de negócios.

### Principais Endpoints da API (`/api/v1/`)

| Método | Endpoint | Descrição | Requer Auth? |
| :--- | :--- | :--- | :--- |
| `POST` | `/authentication/token/` | Obtém os tokens (refresh, access) | ❌ Não |
| `POST` | `/authentication/token/refresh/` | Atualiza um access token | ❌ (Usa Refresh Token) |
| `GET` | `/products/` | Lista todos os produtos | ✅ Sim |
| `POST` | `/products/` | Cria um novo produto | ✅ Sim |
| `GET` | `/products/<id>/` | Detalha um produto | ✅ Sim |
| `PUT` | `/products/<id>/` | Atualiza um produto | ✅ Sim |
| `DELETE` | `/products/<id>/` | Deleta um produto | ✅ Sim |
| `GET, POST` | `/suppliers/` | Lista ou cria fornecedores | ✅ Sim |
| `GET, POST` | `/categories/` | Lista ou cria categorias | ✅ Sim |
| `GET, POST` | `/inflows/` | Lista ou cria entradas de estoque | ✅ Sim |
| `GET, POST` | `/outflows/` | Lista ou cria saídas de estoque | ✅ Sim |

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python
* **Framework Web:** Django
* **API:** Django Rest Framework (DRF)
* **Autenticação API:** DRF Simple JWT (JSON Web Tokens)
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
* **Banco de Dados:** SQLite3 (padrão de desenvolvimento)
* **Testes de API:** Postman

---

## 🚀 Guia de Instalação e Execução

Siga os passos abaixo para executar o projeto em seu ambiente local.

### Requisitos

* Python (3.7 ou superior)
* Git