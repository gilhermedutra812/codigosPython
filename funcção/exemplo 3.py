def calculaImposto(sal,imposto = False):

    """
    função que calcula o imposto de um funcionario
    \nsal: parametro que recebe o salario do funcionario
    \nimposto: parametro opcional que permite mudar o valor do imposto
    """
    if imposto:
        desconto = float(input("qual a porcentagem do imposto: "))
    else:
        desconto = 20

    desconto = desconto/100
    return sal - (sal * desconto)

salario = float(input("informe seu salario: "))

print(f"seu salario com desconto é: R${calculaImposto(salario,True)}")