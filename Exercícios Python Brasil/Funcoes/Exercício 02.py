def funcao(n):
	for i in range(1,n+1):
		temp = ''
		for j in range(1,i+1):
			temp += f'{j} '
		print(temp)
funcao(6)
