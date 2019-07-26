""" 
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. """


while True:
  anos = 0
  habitantesA = int(input('Informe os habitantes da cidade A: '))
  if(type(habitantesA) == int):
    taxaA = float(input('Informe a taxa de crescimento para habitantes da cidade A: '))
  else:
    print(f'{habitantesA} é inválido!')

  habitantesB = int(input('Informe os habitantes da cidade B: '))
  if(type(habitantesB) == int):
    taxaB = float(input('Informe a taxa de crescimento para habitantes da cidade B: '))
  else:
    print(f'{habitantesB} é inválido!')

  while habitantesA <= habitantesB:
    habitantesA += habitantesA * taxaA
    print(f'A {habitantesA:.0f} Habitantes')
    habitantesB += habitantesB * taxaB
    print(f'B {habitantesB:.0f} Habitantes')
    anos += 1

  print(f'Em {anos} anos a população A ultrapassa a B')
  resp = input('Continuar? S/N ')
  if(resp == 'N'):
      break