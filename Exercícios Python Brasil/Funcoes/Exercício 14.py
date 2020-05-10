import itertools
import numpy as np
def isMagick(quadrado):
	nRow = int(len(quadrado)**.5)
	# Armazenar o valor, pois ele tem q ser igual em todas
	k = sum(quadrado[0:nRow])
	# Converter para matriz
	auxiliar = list()
	for i in range(nRow):
		auxiliar.append(quadrado[nRow*i:nRow*(i+1)])
	quadrado = np.array(auxiliar); del auxiliar
	# Testar todas linhas
	for i in range(nRow):
		if sum(quadrado[i,:])!=k:
			return False
	# Testar todas colunas
	for j in range(nRow):
		if sum(quadrado[:,j])!=k:
			return False
	# Testar diagonal principal
	soma = 0
	for i in range(nRow):
		soma+=quadrado[i,i]
	if soma!=k:
		return False
	soma = 0
	for i in range(nRow):
		soma+=quadrado[nRow-i-1,i]
	if soma!=k:
		return False
	return True
def imprimirQuadrado(quadrado):
	cont = 0
	print('Quadrado:\n\t',end='')
	for i in range(len(quadrado)):
		print(f'{quadrado[i]}\t',end='')
		cont+=1
		if cont==3:
			print('\n\t',end='')
			cont=0
	print('-'*18)
def quadradoMagico(n=3):
	lista = list(range(1,n**2+1)) # lista de possibilidades
	valores = itertools.permutations(lista) # permutação para ver todas as possibilidades
	quadrados_magicos = list()
	for valor in valores:
		if isMagick(valor):
			quadrados_magicos.append(valor)
	for quadrado in quadrados_magicos:
		imprimirQuadrado(quadrado)
if __name__ == '__main__':
	quadradoMagico()
