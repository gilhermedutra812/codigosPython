m = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto","setembro","outubro", "novembro", "dezembro")  
temp = []
media = 0

for cont in range(1,13):
    temp.append(float(input(f"informe a temperatura do mes {cont}:")))

media = sum(temp)/cont 
print(f"a media anual de temperatura foi {media:.2f}\n")
for indice,cont in enumerate(temp):
    if cont > media:
        print(f"{mes[indice]:.<10}: {cont}")