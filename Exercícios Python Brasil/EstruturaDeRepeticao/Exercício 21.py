cont=0
numero = int(input("Número: "))
for i in range(1,numero):
	if not(numero%i):
		cont+=1
if cont>1:
	print("Não é primo")
else:
	print("Primo")
