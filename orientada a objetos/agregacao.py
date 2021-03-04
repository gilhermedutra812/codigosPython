class Cliente:
    def __init__(self,nome,telefone,cpf,idade,endereco):
        self.nome = nome 
        self.telefone = telefone
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco

class Conta:
    def __init__(self,numero,cliente,saldo,limite = 1000):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite