import random

x = int(input("largo de lista a desordenar: "))

lista = list(range(1, x + 1))
numeros = []
print(lista)
for _ in range(0, x):
    number = random.randint(1, x)
    while number in numeros:
        number = random.randint(1, x)
    numeros.append(number)
print(numeros)