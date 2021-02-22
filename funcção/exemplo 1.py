from datetime import date
anoAtual = date.today().year
def linha():
    print("-"*50)

nome = str(input("informe seu nome: "))
linha()

idade = int(input("informe sua idade: "))
linha()

print(f"ola {nome} você nasceu no ano de: {anoAtual -  idade}")
linha()