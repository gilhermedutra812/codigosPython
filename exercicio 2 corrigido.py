sal = float(input("informe seu salario no dia: "))
horas = float(input("quantas horas você trabalha por dia? "))

horasTrabalhadas = sal / horas
print("você receberá R$ {} por horas trabalhadas\n\n".format(horasTrabalhadas))