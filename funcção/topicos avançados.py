lista = []
for cont in range(20):
    lista.append(cont)

print(lista)

numeros = [cont**2 for cont in range(20)]
print(numeros)

# utilizar lambda

soma = lambda x,y: x + y

print(soma(4,5))
# trabalhando com função map()
dobro = list(map(lambda x:x*2,lista))

print(dobro)

#trabalhando com função filter
valores = list(range(20,61))
print(valores)

pares = list(filter(lambda num:num%2==0, valores))

print("os valores pares são: \n", pares)