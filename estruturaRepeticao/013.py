""" 
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
 """

base = int(input('Digite a base: '))
if(base == 0):
  final = 0
else:
  potencia = int(input('Digite a potência: '))
  if(potencia != 0):
    final = base
    for i in range(1,potencia):
      final *= base
  else:
    final = 1

print(f'Valor final {final}')


