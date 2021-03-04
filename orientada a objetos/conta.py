class Conta:
    def __init__(self,numero,titular,saldo,limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

        self.__limite = limite

    def depositar(self,valor):
        if valor < 0:
            print("você não pode depositar valor negativo")
        else:
            self.__saldo += valor

    def sacar(self,valor):
        if valor > self.__saldo:
            print("você não pode sacar este valor, seu saldo é {self.__saldo}")
        else:
            self.__saldo -= valor

    def visualisar(self):
        print(f"seu saldo é {self.__saldo}")
        

# outra forma de criar getters e setters
class Conta1:
    def __init__(self,numero,titular,saldo,limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

        self.__limite = limite

# decoradores  "decorator"
# exibir o saldo

    @property
    def saldo(self):
        return f"o seu saldo é R${self.__saldo}"

    #inserindo valoes no atributo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("voce nao pode depositar valores negativos")
        else:
            self.__saldo += valor
            print("valor depositado com sucesso")
