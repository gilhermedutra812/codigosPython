salario = float(input("ifnrome seu salario: "))

while True:
    try:
        salario = float(input("informe seu salario: "))
    except Exception as erro:
        print("informe um valor decimal correto, o erro foi {erro.__class}")
    else:
        break

print(f"seu salario é: R${salario}")


