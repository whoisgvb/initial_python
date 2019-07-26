"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

while True:
  user = input("Digite um usuário: ")
  senha = input("Digite uma senha: ")
  if(user == senha):
    print("Usuário não pode ser igual a senha!")
  else:
    break