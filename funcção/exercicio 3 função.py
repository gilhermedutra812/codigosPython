from random import randint

def sorteio(valor):
    aleatorio = randint(1,100)
    palpite = 1 # contador

    while valor != aleatorio:
        if valor > aleatorio:
            print("o seu palpite é maior do que o valor sorteado")
        elif valor < aleatorio:
            print("o seu palpite é menor do que o valor sorteado")
        palpite +=1
        valor = int(input("informe um novo palpite: "))

    print(f"parabens você acertou o numero com {palpite} palpites")

numero = int(input("diga um palpite de um numero entre 1 e 100: "))
sorteio(numero)