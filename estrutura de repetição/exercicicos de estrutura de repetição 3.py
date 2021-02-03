import time 
import os

totalPessoas = int(input("serão dadas boas vindas para quantas pessoas? "))

#contadores
homens = 0
mulheres = 0

for cont in range (1,totalPessoas+1):
    nome = input("qual seu nome? ")
    sexo = input("qual seu sexo? m/f: ")

    if sexo == "m":
        print(f"bem vindo Sr. {nome}")
        homens += 1
    else:
        print(f"bem vindo Sra. {nome}")
        mulheres += 1

    time.sleep(1)# espera 1 segundo
    os.system("cls")# limpar tela    

print(f"houve um total de {homens}homens  e {mulheres} mulheres")