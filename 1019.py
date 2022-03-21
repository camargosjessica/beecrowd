entrada = int(input())

horas = int(entrada / 3600)
entrada = int(entrada - (horas * 3600))
minutos = int(entrada / 60)
entrada = int(entrada - (minutos * 60))
segundos = int(entrada)

print("{}:{}:{}".format(horas, minutos, segundos))
