""" Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
 """

while True:
  n = int(input('Digite um num: '))
  if(type(n) == int and n < 16):
    fatorial = n
    i = 1

    while(fatorial > 0):
      print(fatorial, end='')
      print(' x ' if fatorial > 1 else ' = ', end='')
      i *= fatorial
      fatorial -= 1

    print(i)
    resp = input('Deseja continuar? S/N\n>>>  ')
    if(resp == 'N'):
      break
  else:
    break