"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
while True:
  nota = int(input("Digite um valor de 0 a 10: "))
  if nota  not in range(1,10):
    print("Digite novamente! ")
  else:
    break

