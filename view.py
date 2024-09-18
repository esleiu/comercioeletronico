from main import Cliente, Clientes, Produto, Produtos, Compra, Compras, Item, Itens
from datetime import datetime

class View:
    # Cliente
    @staticmethod
    def cliente_inserir(nome, email, fone, endereco, senha):
        try:
            if not nome or not email:
                raise ValueError("Nome e e-mail são obrigatórios.")
            a = Cliente(0, nome, email, fone, endereco, senha)
            Clientes.inserir(a)
        except Exception as e:
            print(f"Erro ao inserir cliente: {e}")
            raise

    @staticmethod
    def cliente_listar():
        try:
            return Clientes.listar()
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            raise

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, endereco, senha):
        try:
            a = Cliente(id, nome, email, fone, endereco, senha)
            Clientes.atualizar(a)
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            raise

    @staticmethod
    def cliente_excluir(id):
        try:
            a = Cliente(id, "", "", "", "", "")
            Clientes.excluir(a)
        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")
            raise

    @staticmethod
    def cliente_login(email, senha):
        try:
            clientes = Clientes.listar()
            for cliente in clientes:
                if cliente.get_email() == email and cliente.get_senha() == senha:
                    return cliente
            return None
        except Exception as e:
            print(f"Erro ao realizar login: {e}")
            raise

    # Produto
    @staticmethod
    def produto_listar():
        try:
            return Produtos.listar()
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            raise

    @staticmethod
    def produto_inserir(descricao, preco, estoque):
        try:
            if preco <= 0 or estoque < 0:
                raise ValueError("Preço deve ser positivo e o estoque não pode ser negativo.")
            a = Produto(0, descricao, preco, estoque)
            Produtos.inserir(a)
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
            raise

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque):
        try:
            if preco <= 0 or estoque < 0:
                raise ValueError("Preço deve ser positivo e o estoque não pode ser negativo.")
            a = Produto(id, descricao, preco, estoque)
            Produtos.atualizar(a)
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            raise

    @staticmethod
    def produto_excluir(id):
        try:
            a = Produto(id, "", 0.0, 0)
            Produtos.excluir(a)
        except Exception as e:
            print(f"Erro ao excluir produto: {e}")
            raise

    @staticmethod
    def produto_listar_id(id):
        try:
            produtos = Produtos.listar()  
            for produto in produtos:
                if produto.get_id() == id:
                    return produto
            return None
        except Exception as e:
            print(f"Erro ao buscar produto pelo ID: {e}")
            raise

    # Item
    @staticmethod
    def item_listar():
        try:
            return Itens.listar()
        except Exception as e:
            print(f"Erro ao listar itens: {e}")
            raise

    @staticmethod
    def item_inserir(id_produto, id_compra, qtd, preco):
        try:
            if qtd <= 0 or preco <= 0:
                raise ValueError("Quantidade e preço devem ser positivos.")
            a = Item(0, id_produto, id_compra, qtd, preco)
            Itens.inserir(a)
        except Exception as e:
            print(f"Erro ao inserir item: {e}")
            raise

    @staticmethod
    def item_listar_por_compra(id_compra):
        try:
            itens = Itens.listar()
            return [item for item in itens if item.get_id_compra() == id_compra]
        except Exception as e:
            print(f"Erro ao listar itens por compra: {e}")
            raise

    @staticmethod
    def item_atualizar(id, id_produto, id_compra, qtd, preco):
        try:
            if qtd <= 0 or preco <= 0:
                raise ValueError("Quantidade e preço devem ser positivos.")
            a = Item(id, id_produto, id_compra, qtd, preco)
            Itens.atualizar(a)
        except Exception as e:
            print(f"Erro ao atualizar item: {e}")
            raise

    @staticmethod
    def item_excluir(id):
        try:
            a = Item(id, 0, 0, 0, 0)
            Itens.excluir(a)
        except Exception as e:
            print(f"Erro ao excluir item: {e}")
            raise

    # Compra
    @staticmethod
    def compra_listar():
        try:
            return Compras.listar()
        except Exception as e:
            print(f"Erro ao listar compras: {e}")
            raise

    @staticmethod
    def compra_listar_por_cliente(cliente_id):
        try:
            compras = Compras.listar()
            return [compra for compra in compras if compra.get_id_cliente() == cliente_id]
        except Exception as e:
            print(f"Erro ao listar compras por cliente: {e}")
            raise

    @staticmethod
    def compra_inserir(id_cliente, total):
        try:
            if total <= 0:
                raise ValueError("O total da compra deve ser positivo.")
            a = Compra(0, datetime.now(), total, id_cliente)
            Compras.inserir(a)
            return a.get_id()  
        except Exception as e:
            print(f"Erro ao inserir compra: {e}")
            raise

    @staticmethod
    def compra_atualizar(id, id_cliente, total):
        try:
            if total <= 0:
                raise ValueError("O total da compra deve ser positivo.")
            a = Compra(id, datetime.now(), total, id_cliente)
            Compras.atualizar(a)
        except Exception as e:
            print(f"Erro ao atualizar compra: {e}")
            raise

    @staticmethod
    def compra_excluir(id):
        try:
            a = Compra(id, datetime.now(), 0.0, 0)
            Compras.excluir(a)
        except Exception as e:
            print(f"Erro ao excluir compra: {e}")
            raise

