import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'

)

cod = int(input("informe o codigo da disciplina: "))
nome = str(input("qual o nome da disciplina: ")).lower()
descricao = str(input("qual a descrição da disciplina: ")).lower()
ch = int(input("qual a carga horaria da disciplina: "))

comando = "insert into disciplina values(%s,%s,%s,%s)"

valores = (cod,descricao,nome,ch)

consulta = conexao.cursor()

consulta.execute(comando,valores)

conexao.commit() #gravar os dados no banco

print(consulta.rowcount,"linhas(s) inserida com sucesso!")
conexao.close()