""" Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
 """

n = int(input('Digite um num: '))
fatorial = n
i = 1

while(fatorial > 0):
  print(fatorial, end='')
  print(' x ' if fatorial > 1 else ' = ', end='')
  i *= fatorial
  fatorial -= 1

print(i)




