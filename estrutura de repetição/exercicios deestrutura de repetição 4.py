from os import system

soma = 0

for cont in range(1,11):
    idade = int(input(f"informe a idade da pessoa {cont}:"))

    soma += idade 

    system("cls")
media = soma / cont

if media <= 25:
    print("a turma é jovem")
elif media > 25 and media <= 60:
    print("a turma é adulta")
elif media > 60:
    print("a turma é idosa")

print("\n\n") 