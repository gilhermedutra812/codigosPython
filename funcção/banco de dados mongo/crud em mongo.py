from pymongo import MongoClient
# estabelecendo a conexão
cliente = MongoClient('localhost',27017)

banco = cliente.santander # criando um banco

colecao = banco.clientes # criando collections

while True:
    print(f"{' MENU ':=^40}")
    op = int(input('''
        1. inserir dados
        2. exibir dados
        3. excluir dados
        4. sair

        qual sua escolha: '''))

    if op == 1:
        cpf = int(input("informe o seu cpf(somente números): "))
        nome = str(input("informe o seu nome: ")).title()
        sexo = str(input("informe o seu sexo: (m/f) ")).lower()
        sal = float(input("informe o seu salario: "))
        end = str(input("informe o seu endereço: "))

        # inserindo dados na coolection

        colecao.insert_one({
            'cpf':cpf,
            'nome':f'{nome}',
            'sexo':f'{sexo}',
            'salario':sal,
            'endereco':f'{end}'
        })
        print("\nDados inseridos com sucesso\n")
    elif op == 2:
        print(f"{' exibindo os dados ':-^40}")
        for item in colecao.find():
            print(f"{item['nome']}, possui salario de {item['salario']} e mora no endereço {item['endereco']} com cpf = {item['cpf']} ")
    elif op == 3:
      escolha = int(input("qual o cpf do cliente que deseja excluir: "))
      resultado = colecao.delete_one({
          'cpf':escolha
      })
    print("clientes excluidos: ")
    
    elif op == 4:
        break
    