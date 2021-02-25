lista = []

def listaNomes():
    while True:
        lista.append(str(input("informe um nome: ")).title())
        op = str(input("deseja continuar s/n: ")).lower()
        if op == "n":
            break
def excluiNomes():
    for indice, nomes in enumerate(lista):
        print(f"{indice}: {nomes}")
    pos = int(input("qual a posição da pessoa que você deseja excluir? "))
    print("excluido com sucesso!\n")
    lista.pop(pos) 

while True:
    print("1. inserir nomes: ")
    print("2. excluir nomes: ")
    print("3. sair")

    op = int(input("qual sua opção: "))
    if op == 1: 
        listaNomes()
    elif op == 2:
        excluiNomes()
    elif op == 3:
        break