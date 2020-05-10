from random import randint
def moldura(nRow=1,nColumn=1):
	if not nRow:
		nRow = 1
	if not nColumn:
		nColumn = 1
	if nRow==1:
		if nColumn==1:
			print('+')
		else:
			print(f'+{(nColumn-2)*"-"}+')
	else:
		if nColumn==1:
			print('+')
		else:
			print(f'+{(nColumn-2)*"-"}+')
		for row in range(nRow-2):
			if nColumn==1:
				print('+')
			else:
				print(f'+{(nColumn-2)*" "}+')
		if nColumn==1:
			print('+')
		else:
			print(f'+{(nColumn-2)*"-"}+')
def main():
	x = int(input('Número de linhas:  '))
	y = int(input('Número de colunas: '))
	moldura(x,y)
if __name__ == '__main__':
	main()
