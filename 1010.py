codigopeca1, nropecas1, valorunt1 = input().split()
codigopeca2, nropecas2, valorunt2 = input().split()

codigopeca1, nropecas1, valorunt1 = int(codigopeca1), int(nropecas1), float(valorunt1)
codigopeca2, nropecas2, valorunt2 = int(codigopeca2), int(nropecas2), float(valorunt2)

valor_pagar = (nropecas1 * valorunt1) + (nropecas2 * valorunt2)

print("VALOR A PAGAR: R$ {:.2f}".format(valor_pagar))
