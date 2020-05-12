# Faça um programa que imprima na tela os números de 1 a 20, 
# um abaixo do outro. Depois modifique o programa para que ele 
# mostre os números um ao lado do outro.
# Para esse exercício vamos utilizar outra estrutura de repetição.
# O For (para)
# sintaxe:
# for variavel in iterator:
#     faz algo
# Onde o iterator pode ser qualquer objeto com essa característica (lista, tupla, range,...)
# 
# Aqui vai imprimir 
for i in range(1,21): # vai gerar um intervalo de 1 a 20
	print(i) # imprime o valor da variavel e quebra a linha

# Aqui imprimir todos na mesma linha
for i in range(1,21):
	print(i,end=" ")
