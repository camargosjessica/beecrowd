entrada = int(input())

ano = int(entrada / 365)
entrada = int(entrada - (ano * 365))
meses = int(entrada / 30)
entrada = int(entrada - (meses * 30))
dias = int(entrada)

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, meses, dias))
