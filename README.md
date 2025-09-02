# Sistema de Comércio Eletrônico em Streamlit

## Descrição do Projeto

Este projeto foi desenvolvido como um trabalho para a matéria de **Programação Orientada a Objetos (POO)**. Trata-se de um sistema de e-commerce simples, porém funcional, que permite o cadastro de produtos, clientes e a realização de compras. A interface gráfica foi construída utilizando a biblioteca **Streamlit**.

O sistema possui duas visões principais:
* **Visão do Administrador (`admin`):** Permite o gerenciamento completo dos dados do sistema, incluindo clientes, produtos, itens de compra e compras.
* **Visão do Cliente (Usuário Comum):** Focada na experiência de compra, permitindo ao cliente navegar pelos produtos, adicionar itens ao carrinho, visualizar seu histórico e cancelar compras.

A persistência dos dados é realizada localmente através de arquivos no formato JSON.

## Funcionalidades

### Acesso Geral
* **Login e Cadastro:** Sistema de autenticação para clientes e um usuário `admin` padrão.
* **Cadastro de Novos Clientes:** Usuários podem criar suas próprias contas.

### Funcionalidades do Administrador (`admin`)
* **Manter Clientes:** Gerenciamento completo (CRUD - Criar, Ler, Atualizar, Excluir) dos clientes cadastrados.
* **Manter Produtos:** Gerenciamento completo de produtos, incluindo descrição, preço e controle de estoque.
* **Manter Compras:** Visualização e gerenciamento das compras realizadas no sistema.
* **Manter Itens:** Gerenciamento dos itens individuais que compõem cada compra.

### Funcionalidades do Cliente
* **Realizar Compra:** Interface para adicionar produtos a um carrinho de compras e finalizar o pedido. O estoque do produto é atualizado automaticamente.
* **Mostrar Compras:** Permite que o cliente logado visualize seu histórico de compras.
* **Cancelar Compras:** O cliente pode selecionar e excluir uma compra de seu histórico, o que também remove os itens associados a ela.

## Estrutura do Projeto

O código está organizado da seguinte forma:

* `index.py`: Arquivo principal que inicializa a aplicação Streamlit e gerencia os menus de navegação.
* `main.py`: Contém as classes de modelo (`Cliente`, `Produto`, `Compra`, `Item`) e as classes de persistência que manipulam os arquivos JSON (`Clientes`, `Produtos`, `Compras`, `Itens`).
* `modelo.py`: Define a classe base abstrata `Modelo`, que serve como um padrão para as classes de persistência.
* `view.py`: Camada de controle que conecta a interface do usuário (UI) com as regras de negócio e a persistência de dados.
* **Arquivos `UI` (`manterclienteUI.py`, `realizarcompraUI.py`, etc.):** Cada arquivo é responsável por construir uma tela específica da interface Streamlit.
* **Arquivos `.json` (`clientes.json`, `produtos.json`, etc.):** Utilizados como "banco de dados" para armazenar as informações.

## Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior
* Pip (gerenciador de pacotes do Python)

### 1. Instalação das Dependências

Primeiro, instale as bibliotecas necessárias. Abra o terminal na pasta raiz do projeto e execute:

```bash
pip install streamlit pandas
```

### 2. Executando a Aplicação

Para iniciar o servidor do Streamlit e abrir a aplicação no seu navegador, execute o seguinte comando no terminal:

```bash
streamlit run index.py
```

### 3. Acessando o Sistema

* **Para acessar como administrador:**
    * **Email:** `admin@admin.com`
    * **Senha:** `admin`

* **Para acessar como cliente:**
    * Você pode se cadastrar na tela "Cadastrar-se" ou usar um dos clientes já presentes no arquivo `clientes.json`.