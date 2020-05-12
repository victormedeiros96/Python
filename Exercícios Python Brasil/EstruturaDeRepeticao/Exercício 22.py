cont=0
numero = int(input("Número: "))
for i in range(1,numero):
	if not(numero%i):
		cont+=1
if cont>1:
	print('Divisível por:')
	for i in range(1,numero+1):
		if not(numero%i):
			print(i)			
else:
	print("Primo")
