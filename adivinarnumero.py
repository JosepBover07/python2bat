import random

minimo = 1
maximo = 10

numeroelegido = random.randint(minimo, maximo)

numeropedido = int(input(f"elige un numero {minimo} y {maximo}"))

if numeroelegido == numeropedido:
    print("enhorabuena, lo has acertado")
else:
    print(f"no has acertado el numero. Era el {numeroelegido}")
