flag = True
while flag:
	n=-1
	while not(n in range(1,17)):
		n = int(input("Numero: "))
	fatorial = 1
	for i in range(1,n+1):
		fatorial*=i
	print(fatorial)
	aux = input("Deseja continuar? (s para sim, n para não) : ").lower()
	flag = (False if ((aux=="n")or(aux=="não")or(aux=="nao")) else True)

