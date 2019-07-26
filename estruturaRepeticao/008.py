""" Faça um programa que leia 5 números e informe a soma e a média dos números.
 """
r = []
for i in range(6):
  num = int(input(f'Informe o {i}º numero: '))
  r.append(num)
  #r.insert(i, num)

soma = (r[0] + r[1] + r[2] + r[3] + r[4])
media = (r[0] + r[1] + r[2] + r[3] + r[4])/6

print(f'A soma é {soma:.0f} e a média {media}')