def calculaImposto(sal,imposto):
    imposto = imposto/100
    novoSalario = sal - (sal*imposto)
    
    return novoSalario

salario = float(input("informe seu salario: "))
desconto = float(input("qual o valor da porcentagem de imposto: "))

print(f"seu salario liquido com {desconto}% de desconto é de R${calculaImposto(salario,desconto)}")
