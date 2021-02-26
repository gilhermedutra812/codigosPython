import pymysql

# estabelecer conexão
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'

)

consulta = conexao.cursor() # a função cursor é importante pois permite interagir com o banco de dados :) 

sql = "select * from aluno"
consulta.execute(sql)

'''
for itens in consulta:
    print(itens)
'''
#exibir a consulta personalizada
resultado = consulta.fetchall()

for itens in resultado:
    print(f"olá {itens[1]} você mora no bairro {itens[4]}")

conexao.close()

