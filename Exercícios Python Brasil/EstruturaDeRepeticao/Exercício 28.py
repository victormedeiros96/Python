quantidade = 0
while True:
	aux = input('Qual a quantidade de CDS? ')
	try:
		aux = int(aux)
		if aux>0:
			quantidade = aux
			break
	except Exception as e:
		print(e)
		print('A quantidade deve ser positiva')
total = 0
for i in range(quantidade):
	valor = -1
	while not(valor>=0):
		aux = input('Qual o preço do CD? ')
		try:
			aux = int(aux)
			if aux>=0:
				valor = aux
		except Exception as e:
			print(e)
			print('Por favor, entre com um valor válido')
			continue
	total+=valor
print(f'''Quantidade de CDs: {quantidade}
Média de custo por CDS: {total/quantidade:g}''') 
