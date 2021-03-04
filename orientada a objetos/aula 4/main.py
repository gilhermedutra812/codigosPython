from associacao import Celular, Pessoa

smartphone = Celular("xiaomi",1500)

p1 = Pessoa("clotilde",45,"rua 71 vila cascavel")

print(f"{p1.nome} mora no endereço {p1.endereco} e tem {p1.idade} anos")

p1.celular = smartphone

print(f"{p1.nome} possui um celular da marca {p1.celular.marca} e custou R$ {p1.celular.valor}")