""" 
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""
pares = []
impares = []
for i in range(1,11):
  n = int(input(f'Digite o {i}º numero: '))
  if(n % 2 == 0):
    pares.append(n)
  else:
    impares.append(n)

print(f'impares: {impares}\npares: {pares}')





