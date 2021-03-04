class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        self.__cpf = ""

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,valor):
        if len(valor) != 11:
            print("o CPF precisa ter 11 numeros e tem que ser somente números")
        elif valor.isnumeric():
            self.__cpf = valor
        else:
            print("insira somente numeros!!!!")

    def exibirDados(self):
        print(f"nome: {self.nome}")
        print(f"cpf: {self.__cpf}")
class Aluno(Pessoa):
    def __init__(self,nome,matricula,curso="nenhuma"):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso

    def exibirDados(self):
        super().exibirDados()
        print(f"matricula: {self.matricula}")
        print(f"curso: {self.curso}")


class Professor(Pessoa):
    def __init__(self,nome, salario, ch):
        super().__init__(nome)
        self.salario = salario
        self.ch = ch 

    def exibirDados(self):
        super().exibirDados()
        print(f"salario: R${self.salario}")
        print(f"carga horaria: {self.ch}")
