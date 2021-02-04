cont = 1
soma = 0 
contNegativos = 0

while cont <= 10:
    valor = int(input(f"informe o {cont}º valor: "))

    if valor < 0:
        contNegativos += 1
    else:
        soma += valor
    cont += 1

print(f"A soma dos valores positivos é {soma}")
print(f"a quantidade dos valores negativos é {contNegativos}")
    