from os import system 
frutas = list()

for cont in range(1,6):
    frutas.append(input("informe o nome de uma fruta: "))

while True:
    system("cls")
    print(f"{'lista de frutas':*^30}\n")

    for indice, itens in enumerate(frutas):
        print(f"{indice:.<10} {itens}")
    print("\n")
    print("0. terminar")
    print("1. inserir uma fruta")
    print("2. excluir uma fruta")
    op = int(input("o que deseja fazer: "))

    if op == 0:
        break
    elif op ==1:
        frutas.append(input("informe um nova fruta: "))
    elif op ==2:
        valor = int(input("qual  a posição da fruta você dejesa remover? "))
       frutas.pop(valor)


print("obrigado por usar o sistema!\n\n")