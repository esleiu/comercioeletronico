from abc import ABC, abstractmethod 

class Modelo(ABC):

    objetos = []  # Atributo da classe e não de uma instância da classe

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.get_id() > id: 
                id = x.get_id()
        id += 1
        obj.set_id(id)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos 

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.objetos:
            if x.get_id() == id: 
                return x
        return None    

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())  # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x:
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass    

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass
