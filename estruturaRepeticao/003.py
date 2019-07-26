""" 
Faça um programa que leia e valide as seguintes informações:
  Nome: maior que 3 caracteres;
  Idade: entre 0 e 150;
  Salário: maior que zero;
  Sexo: 'f' ou 'm';
  Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
  nome = input('Digite seu nome: ')
  print(f'Nome: {nome}' if len(nome) >= 3 else 'Nome inválido')
  idade = int(input('Digite sua idade: '))
  print(f'Idade: {idade}' if idade > 0 and idade < 150 else 'Idade inválido')
  salario = int(input('Digite seu salário: '))
  print(f'Salário R$: {salario}' if salario > 0 else 'Salário inválido')
  sexo = input('Digite seu sexo: ')
  print(f'Sexo: {sexo}' if sexo == 'm' or sexo == 'f' else 'Sexo inválido')
  eCivil = input('Digite seu estado civil: ')
  opCivil = ('s', 'c', 'v', 'd')
  print(f'Estado civil: {eCivil}' if eCivil in opCivil else 'Estado civil inválido')
  resp = input("Deseja continuar? S/N ")
  if(resp == 'N'):
    break
  







  