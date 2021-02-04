while True:
    valor = int(input("informe um valor qualquer: "))

    if valor < 0:
        break

    if valor > 100:
        print("limite excedido")
    elif valor > 10:
        print(f"o quadrado de {valor} é {valor**2}")
    elif valor > 5:
        print(f"o cubo de {valor} é {valor**3}")     
