from agregacao import Cliente, Conta

c1 = Cliente("madrugada","98 91234-5678", "123.456.789-98", "rua das patativas 35 bairro ilhinha")

conta1 = conta(1234,c1,1100,2000)

print(f"{conta1.titular.nome} possui saldo de R${conta1.saldo} e mora no endereço{conta1.titular.endereco} e possui telefone{conta1.titular.telefone} e um limite de R${conta1.limite}\n ")