cont = 0
numero = int(input(f'Numero: '))
for i in range(2,numero):
	if not(numero%i):
		print('Não é Primo')
		exit()
print('É primo')
