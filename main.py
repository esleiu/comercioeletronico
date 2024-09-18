import json
from datetime import datetime
from modelo import Modelo


# classes

# cliente
class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str, endereco: str, senha: str):
        if nome == "" or email == "" or senha == "":
            raise ValueError("nome, e-mail e senha são obrigatórios")
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__endereco = endereco
        self.__senha = senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__endereco} - {self.__senha}"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_fone(self):
        return self.__fone

    def set_fone(self, fone):
        self.__fone = fone

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

# produto
class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int):
        if preco < 0:
            raise ValueError("o preço não pode ser negativo")
        if estoque < 0:
            raise ValueError("o estoque não pode ser negativo")
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__preco} - {self.__estoque}"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        if preco < 0:
            raise ValueError("o preço não pode ser negativo")
        self.__preco = preco
    
    def get_estoque(self):
        return self.__estoque

    def set_estoque(self, estoque):
        if estoque < 0:
            raise ValueError("o estoque não pode ser negativo")
        self.__estoque = estoque

# item
class Item:
    def __init__(self, id: int, id_produto: int, id_compra: int, qtd: int, preco: float):
        self.__id = id
        self.__id_produto = id_produto
        self.__id_compra = id_compra
        self.__qtd = qtd
        self.__preco = preco

    def __str__(self):
        return f"{self.__id} - produto id: {self.__id_produto} - compra id: {self.__id_compra} - quantidade: {self.__qtd} - preço: {self.__preco}"

    def to_json(self):
        return {
            'id': self.__id,
            'id_produto': self.__id_produto,
            'id_compra': self.__id_compra,
            'qtd': self.__qtd,
            'preco': self.__preco
        }

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_id_produto(self):
        return self.__id_produto

    def set_id_produto(self, id_produto):
        self.__id_produto = id_produto

    def get_id_compra(self):
        return self.__id_compra

    def set_id_compra(self, id_compra):
        self.__id_compra = id_compra

    def get_qtd(self):
        return self.__qtd

    def set_qtd(self, qtd):
        self.__qtd = qtd

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

# compra
class Compra:
    def __init__(self, id: int, data: datetime, total: float, idcliente: int): 
        if total < 0:
            raise ValueError("o total deve ser positivo")
        self.__id = id
        self.__data = data
        self.__total = total
        self.__idcliente = idcliente

    def to_json(self):
        return {
            'id': self.__id,
            'data': self.__data.strftime('%d/%m/%Y %H:%M'),
            'total': self.__total,
            'idcliente': self.__idcliente
        }
    
    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__total} - {self.__idcliente}"

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_total(self):
        return self.__total

    def set_total(self, total):
        if total < 0:
            raise ValueError("o total deve ser positivo")
        self.__total = total

    def get_id_cliente(self):
        return self.__idcliente

    def set_id_cliente(self, idcliente):
        self.__idcliente = idcliente


# persistência - cliente
class Clientes(Modelo):
    @classmethod
    def salvar(cls):
        try:
            with open("clientes.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default=lambda o: o.__dict__)
        except IOError as e:
            print(f"erro ao salvar clientes: {e}")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"], obj["_Cliente__endereco"], obj["_Cliente__senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

# persistência - itens
class Itens(Modelo):
    @classmethod
    def salvar(cls):
        try:
            with open("itens.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default=lambda o: o.to_json())
        except IOError as e:
            print(f"erro ao salvar itens: {e}")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("itens.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    i = Item(
                        obj['id'], 
                        obj['id_produto'], 
                        obj['id_compra'], 
                        obj['qtd'], 
                        obj['preco']
                    )
                    cls.objetos.append(i)
        except FileNotFoundError:
            pass

# persistência - produtos
class Produtos(Modelo):
    @classmethod
    def salvar(cls):
        try:
            with open("produtos.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default=lambda o: o.__dict__)
        except IOError as e:
            print(f"erro ao salvar produtos: {e}")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    p = Produto(
                        obj["_Produto__id"], 
                        obj["_Produto__descricao"], 
                        float(obj["_Produto__preco"]),  # conversão para float
                        int(obj["_Produto__estoque"])   # conversão para int
                    )
                    cls.objetos.append(p)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"erro ao abrir o arquivo de produtos: {e}")

# persistência - compras
class Compras(Modelo):
    @classmethod
    def salvar(cls):
        try:
            with open("vendas.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default=lambda o: o.to_json())
        except IOError as e:
            print(f"erro ao salvar vendas: {e}")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                texto_arquivo = json.load(arquivo)
                for obj in texto_arquivo:
                    v = Compra(
                        obj['id'], 
                        datetime.strptime(obj['data'], "%d/%m/%Y %H:%M"),  
                        float(obj['total']),  # conversão para float
                        obj['idcliente']
                    )
                    cls.objetos.append(v)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"erro ao abrir o arquivo de vendas: {e}")
