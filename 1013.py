a, b, c = input().split()

a, b, c = int(a), int(b), int(c)

calculo = (a + b + abs(a - b)) / 2
calculo_2 = (calculo + c + abs(calculo - c)) / 2

print("{:.0f} eh o maior".format(calculo_2))
