""" Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
 """

n = int(input("Digite os laços: "))
if(n > 1):
  maior = 0
  menor = 0
  for i in range(n):
    x = int(input("Digite um número: "))
    if(x > 1 and x < 1000):
      maior = (maior if maior != 0 and maior > x else x)
      menor = (menor if menor != 0 and menor < x else x)
    else:
      break
  if(i+1 == n):
    print (f'O maior valor digitado foi {maior} e o menor foi {menor}')
  else:
    print('Você quebrou o programa')
else:
    print('Tente amanhã')

