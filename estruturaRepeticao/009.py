""" Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""

numeros = [x for x in range(1,51)]
impares = [i for i in numeros if i % 2 != 0]
print(impares)


