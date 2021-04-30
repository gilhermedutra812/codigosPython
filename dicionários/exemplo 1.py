produtos = [
    "pão 1kg", 9.00,
    "leite",5.59,
    "café",3.99,
    "açúcar",2.25,
    "azeite",16.99,
    "arroz kg",19
]

print("-"*40)
print(f"{'lista de compras':^40}")
print("-"*40)

for indice,itens in enumerate(produtos):
    if indice%2==0:
        print(f"{itens:.<30}",end="")
    else:
        print(f"{itens:>8}")

print("-"*40)