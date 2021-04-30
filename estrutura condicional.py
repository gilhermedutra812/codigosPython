nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
nota3 = float(input("digite a nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("voce passou, :)")
elif media == 7:
    print("passou arrastado. :|")
else:
    print("infelizmente não passou, :(")