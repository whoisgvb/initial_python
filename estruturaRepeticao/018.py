""" 
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
 """
n = int(input("Digite os laços: "))
maior = 0
menor = 0
for i in range(n):
   x = int(input("Digite um número: "))
   maior = (maior if maior != 0 and maior > x else x)
   menor = (menor if menor != 0 and menor < x else x)

print (f'O maior valor digitado foi {maior} e o menor foi {menor}')