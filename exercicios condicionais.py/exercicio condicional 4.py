km = float(input("quantos km o carro faz com 1 litro? "))
restante = float(input("quantos litros de combustivel há no momento? "))
distancia = float(input("qual a distancia que voce deseja percorrer? "))

if distancia / km < restante:
    print("pode ir tranquilo que da pra chegar no destino")
else:
    print("voce vai precisar abastecer {:.2f} litros\n\n".format(distancia/km - restante))