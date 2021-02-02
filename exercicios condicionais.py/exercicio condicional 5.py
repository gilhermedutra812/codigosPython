vPermitida = float(input("qual é a velocidade permitida? "))
vMotorista = float(input("qual a velocidade do motorista? "))

vPermitida = (vPermitida * 0.2) + vPermitida

vPermitida50 = (vPermitida * 0.5) + vPermitida

if vMotorista <= vPermitida:
    print("tudo certo, não precisa pagar multa")
elif vMotorista > vPermitida and vMotorista <= vPermitida:
    print("voce cometeu infração média\nAssin irá pagar R$85.00 e receber 4 pontos na carteira")
elif vMotorista > vPermitida and vMotorista <= vPermitida50:
    print("voce cometeu uma infração grave\nAssim irá pagar R$127.00 e receber 5 pontos na carteira")
elif vMotorista > vPermitida50:
    print("voce cometeu uma infração gravissima\nAssim irá pagar 574.00 alem de receber 7 pontos carteira\n Ter carteira apreendida e \nTer o direito de dirigir suspenso")