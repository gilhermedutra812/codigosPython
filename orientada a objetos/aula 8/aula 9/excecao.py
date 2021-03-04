num1 = int(input("informe um valor numerico: "))
num2 = int(input("informe outro valor numerico: "))

try:
    resultado = num1/num2
except Exception as erro:
    print("deu erro man, tenta de nvo ai pls: {erro.__class__}")
else:
    print(f"o resultado é {resultado}: ")