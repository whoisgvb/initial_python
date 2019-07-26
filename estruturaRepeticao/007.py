""" 
Faça um programa que leia 5 números e informe o maior número.
 """
r = []
for i in range(6):
  num = int(input(f'Informe o {i}º numero: '))
  r.append(num)
  #r.insert(i, num)

print(r)