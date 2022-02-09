funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

calculo_salario = horas_trabalhadas * valor_hora

print("NUMBER = {}".format(funcionario))
print("SALARY = U$ {:.2f}".format(calculo_salario))
