class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def mostraClasse(self):
        print(f"{self.nomeClasse} = seu nome é {self.nome}")

class Aluno(Pessoa): #subclasse
    def __init__(self,nome,idade,matricula):
        Pessoa.__init__(self,nome,idade)
        self.matricula = matricula
        

class Professor(Pessoa): #subclasse
    def mostraProfessor(self):
        print(f"{self.nomeClasse} = sou professor e meu nome é {self.nome}")

