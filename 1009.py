funcionario = str(input())
salario = float(input())
vendas = float(input())

comissao = (vendas * 15) / 100
recebimento = salario + comissao

print("TOTAL = R$ {:.2f}".format(recebimento))
