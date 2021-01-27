produto1 = int(input("informe o valor do produto 1: "))
produto2 = int(input("informe o valor do produto 2: "))
produto3 = int(input("informe o valor do produto 3:"))

total = int(produto1 + produto2 + produto3)
print("o preço total é: ", total)

desconto = int(total * 20)/100
print("o desconto é de " ,desconto, "reais")

totalPago = int(total - desconto)
print("o total a ser pago é ", totalPago)