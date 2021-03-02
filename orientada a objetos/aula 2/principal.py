from funcionario import Funcionario

f1 = Funcionario("rosangela","auxiliar administratuivo", 1600)

f1.relatorio()

f2 = Funcionario("alberto","pedreiro")

print(f"o salario de {f2.nome} é R$ {f2.sal}")
f2.nome = "jorge"
print(f"o salario de {f2.nome} é R$ {f2.sal}")