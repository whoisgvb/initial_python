""" Altere o programa anterior para mostrar no final a soma dos números.
 """
soma = 0
n1 = int(input('Digite o primeiro numero INTEIRO: '))
n2 = int(input('Digite o segundo numero INTEIRO: '))

for i in range(n1+1,n2):
  while(n1<n2-1):
    n1=n1+1
    soma = n1 + soma
      
print(f'Resultado: {soma}')