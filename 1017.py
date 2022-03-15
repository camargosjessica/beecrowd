tempo = int(input())
velocidade = int(input())

por_litro = 12

percorrido = tempo * velocidade

litro_gasto = percorrido / por_litro

print("{:.3f}".format(litro_gasto))
