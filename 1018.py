entrada = int(input())
lista_notas = [100, 50, 20, 10, 5, 2, 1]

for valor_nota in lista_notas:
    quantidade_notas = int(entrada / valor_nota)
    entrada = entrada - (quantidade_notas * valor_nota)
    print("{} nota(s) de R$ {},00".format(quantidade_notas, valor_nota))
