# Para esse primeiro exercício vamos usar uma estrutura de repetição chamada while (enquanto)
# Segue essa sintaxe:
# while (condição): 
#     ExercutaTalAção # onde condição pode ser o retorno de uma operação, ou mesmo um valor booleano
while True: # Nesse caso, é enquanto Verdade. Ou seja, sempre retorna ao início do laço
	valor = input('Digite uma nota entre 0 e 10: ')
	try: #tentar
		valor = float(valor)
	except ValueError:
		print(f'{valor} não é um número')
		continue
	if ((valor>0) and (valor<=10)):
		exit()
