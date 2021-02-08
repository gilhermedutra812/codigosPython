from os import system 

numeros = []

for cont in range(1,11):
    numeros.append(int(input(f"informe o valor {cont}: ")))

system("cls")

for indice,cont in enumerate(numeros):
    print(f"{indice:-<10}>{cont}")

pos1 = int(input("escolha a 1º posição"))    
pos2 = int(input("escolha a 2º posição"))

print(f"{numeros[pos1]} x {numeros[pos2]} = {numeros[pos1] * numeros[pos2]}")
print(f"{numeros[pos1]} + {numeros[pos2]} = {numeros[pos1] + numeros[pos2]}")
print(f"{numeros[pos1]} - {numeros[pos2]} = {numeros[pos1] - numeros[pos2]}")
print(f"{numeros[pos1]} / {numeros[pos2]} = {numeros[pos1] / numeros[pos2]}")
print(f"{numeros[pos1]} ** {numeros[pos2]} = {numeros[pos1] ** numeros[pos2]}")