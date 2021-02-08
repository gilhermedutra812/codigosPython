valores = list()

for cont in range(1,11):
    valores.append(int(input(f"informe o valor {cont}:")))

print(valores)

for cont in valores:
    if cont % 2==0:
        valores.remove(cont)

print(f"lista sem os valores pares: {valores}\n\novembro")