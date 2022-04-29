entrada = float(input())
lista_notas = [100, 50, 20, 10, 5, 2]
lista_moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for valor_nota in lista_notas:
    quantidade_notas = int(entrada / valor_nota)
    entrada = entrada - (quantidade_notas * valor_nota)
    print("{} nota(s) de R$ {}.00".format(quantidade_notas, valor_nota))

print("MOEDAS:")
for valor_moeda in lista_moedas:
    quantidade_moedas = int(entrada / valor_moeda)
    entrada = entrada - (quantidade_moedas * valor_moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantidade_moedas, valor_moeda))
