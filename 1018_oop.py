class Valores:
    quantidade: int = 0
    nota: int = 0

    def __init__(self, nota: int, quantidade: int):
        self.quantidade = quantidade
        self.nota = nota


entrada = int(input())
lista_notas = [100, 50, 20, 10, 5, 2, 1]
lista_resultados = []

for valor_nota in lista_notas:
    quantidade_notas = int(entrada / valor_nota)
    resultado_notas = Valores(valor_nota, quantidade_notas)
    entrada = entrada - (quantidade_notas * valor_nota)
    lista_resultados.append(resultado_notas)

for resultado in lista_resultados:
    print("{} nota(s) de R$ {},00".format(resultado.quantidade, resultado.nota))
