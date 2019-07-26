""" 
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
 """
 # AJUDA algumas fontes definem como 0 o primeiro termo, 1 o segundo termo e do terceiro em diante é a soma dos dois termos anteriores, que é uma definição diferente dos dados da questão. No fim das contas, isso não importa muito, pois a lógica é a mesma, só precisa de alguns pequenos ajustes. #

fib = [1,1]
i = 0
num = int(input("Entre com um número: "))

while num > len(fib):
	fib.append(fib[i] + fib[i+1])
	i+=1

print (f'Fibonacci {fib[num-1]}')
