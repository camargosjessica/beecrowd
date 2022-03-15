x1, y1 = input().split()
x2, y2 = input().split()

x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

soma1 = (x2 - x1) ** 2
soma2 = (y2 - y1) ** 2

resultado = (soma1 + soma2) ** 0.5

print("{:.4f}".format(resultado))
