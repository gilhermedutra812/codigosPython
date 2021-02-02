massa = float(input("informe seu peso corporal: "))
altura = float(input("informe sua altura corporal: "))

altura2 = altura * altura
imc = (massa / altura2)

if imc < 16:
    print("magreza grave")
elif imc >= 16 or imc <= 17:
    print("magreza moderada")
elif imc >= 17 or imc <= 18.5:
    print("magreza leve")
elif imc >= 18.5 or imc <= 25:
    print("saudavel :)")
elif imc >= 25 or imc <= 30:
    print("sobrepeso")
elif imc >= 30 or imc <= 35:
    print("obesidade grau 1")
elif imc >= 35 or imc <= 40:
    print("obesidade grau 2(severa)")
elif imc >= 40:
    print("obesidade grau 3(morbida)")