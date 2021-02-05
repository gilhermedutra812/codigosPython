pessoas = ["fabio","carlos","regina","vanusa"]

print(type(pessoas))

print(pessoas)

pessoas[1] = "sergio"

#adicionando elementos

pessoas.append("sarah") #adiciona no final
pessoas.insert(2,"flávio") #adiciona em qualquer lugar

for chave, valor in enumerate(pessoas):
    print(f"{chave:.<5}{valor}")

#removendo elementos
pessoas.pop()# remove o ultimo elemento
pessoas.pop(1)# 
pessoas.remove("flávio")

print(pessoas)

#copiando listas
pessoasBkp = pessoas[:]
pessoasBkp.append("jeronimo")
print("\n\n", pessoas)
print(pessoasBkp,"\n\n")

pessoas.clear()# limpa a lista
del(pessoas)# excluir a variavel lista
print(pessoas,"\n\n")