pessoas = ("carlos","Mario","luisa","Felipe")

print(type(pessoas))
print(pessoas)

print(pessoas[1]) 

for itens in pessoas:
    print(itens)

print("luisa está na posição ", pessoas.index("luisa"))

for indice,itens in enumerate(pessoas):
    print(f"{indice:.<20}{itens}")