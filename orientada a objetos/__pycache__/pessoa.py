from datetime import date

class Pessoa:
    # atributos
    nome = "josé"
    idade = "45"
    altura = "1.65"

    #metodo
    def falar(self, texto):
        print(texto)

    def andar(self):
        print("tô andando!!")

    def deitar(self):
        pass
    
    def calculaAno(self,idade):
        anoAtual = date.today().year
        print(f"você nasceu no ano de {anoAtual - idade}")

