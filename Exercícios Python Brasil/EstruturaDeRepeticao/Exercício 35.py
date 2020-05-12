
primos = list()
numero = int(input(f'Numero: '))
for j in range(numero):
	cont = 0
	for i in range(2,j):
		if not(j%i):
			cont+=1
	if not cont:
		primos.append(j)
print(primos)
