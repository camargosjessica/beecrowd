a = float(input())
b = float(input())

peso_a = 3.5
peso_b = 7.5

media_peso = peso_a + peso_b

nota_a = (a * peso_a) / media_peso
nota_b = (b * peso_b) / media_peso

nota_final = nota_a + nota_b

print("MEDIA = {:.5f}".format(nota_final))
