from random import randint
aleatorio = []
for cont in  range(1,21):
    aleatorio.append(randint(1,900))

for cont in range(3,0,-1):
    print(f"você tem {cont} chances para descobrir um dos valores da lista")
    op = int(input("informe um valor: "))

    if op in aleatorio:
        print(F"{'PARABENS':^40}")
        print("voce conseguiu encontrar o valor")

        break
    else:
        print("eita, ainda não é esse valor, você consegue, ; ")
print(aleatorio,"\n\n")