import pymysql

conexao = pymysql.connect(
    host = 'locahost',
    user = 'root',
    password = '',
    database = 'ecommerce'

)

while True:
    print(f"{'O QUE VOCÊ DESEJA FAZER'=^20}")

    op = int(input('''

    1. inserir dados 
    2. consultar dados
    3. sair

    '''))
    if op == 1:
        cod = int(input("informe o código do produto: "))
        preco = float(input("informe o preço do produto: "))
        tipo = str(input("informe o tipo do produto: "))

    tabela = "create table produtos(

    elif op == 2:
        pass

    elif op == 3:
        break

 