""" Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. """

anos = 0
habitantesA = 80000
habitantesB = 200000


while habitantesA <= habitantesB:
  habitantesA += habitantesA * 0.03
  print(f'A {habitantesA:.0f} Habitantes')
  habitantesB += habitantesB * 0.015
  print(f'B {habitantesB:.0f} Habitantes')
  anos += 1

print(f'Em {anos} anos a população A ultrapassa a B')
