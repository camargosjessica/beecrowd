class Nota:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

    def get_nota_media(self):
        return self.valor * self.peso


nota_a = Nota(float(input()), 2.0)
nota_b = Nota(float(input()), 3.0)
nota_c = Nota(float(input()), 5.0)

media_peso = nota_a.peso + nota_b.peso + nota_c.peso

resultado_a = nota_a.get_nota_media() / media_peso
resultado_b = nota_b.get_nota_media() / media_peso
resultado_c = nota_c.get_nota_media() / media_peso

nota_final = resultado_a + resultado_b + resultado_c

print("MEDIA = {:.1f}".format(nota_final))
