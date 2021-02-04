from datetime import date

anoAtual = date.today().year
while True:
    nascimento = int(input("informe o ano do seu nascimento: "))

    idade = anoAtual - nascimento

    if idade >= 18:
     print(f"voce possui {idade} anos, prossiga com a inscrição\n")
     break
    else:
        print(f"voce possui {idade} anos, voce ainda não pode se inscrever\n")