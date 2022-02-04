a = float(input())
b = float(input())
c = float(input())

peso_a = 2.0
peso_b = 3.0
peso_c = 5.0

media_peso = peso_a + peso_b + peso_c

nota_a = (a * peso_a) / media_peso
nota_b = (b * peso_b) / media_peso
nota_c = (c * peso_c) / media_peso

nota_final = nota_a + nota_b + nota_c

print("MEDIA = {:.1f}".format(nota_final))
