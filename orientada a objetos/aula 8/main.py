from polimorfismo import Pessoa, Aluno, Professor

p1 = Pessoa("jose")

p1.cpf = "rerwe"

print(len(p1.cpf))

p1.exibirDados()

aluno1 = Aluno("joana", 12345, "linguas")

aluno1.exibirDados()

prof = Professor("emergino", 2000,44)

prof.exibirDados()

