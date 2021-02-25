def somatorio(valor):
    soma = 0
    for cont in range(1,valor+1):
        soma += cont
        if cont == valor:
            print(f"{cont}={soma}")
        else:
            print(f"{cont}",end="+") 
while True:
    numero = int(input("informe o  numero inteiro qualquer: "))
    if numero > 0:
        somatorio(numero)
    else:
        print("informe um valor positivo")

    op = str(input("deseja continuar s/n: ")).lower()

    if op == "n":
        break