numeros = list()
while True:
	temp = float(input("Adicione um número no conjunto (-1 para parar de incluir): "))
	if temp==-1:
		break
	elif temp<0 or temp>1000:
		print("Número não aceito. Por favor, um número entre 0 e 1000")
	else:
		numeros.append(temp)
soma = 0
menor = 0
maior = 0
for i in numeros:
	soma+=i
	if menor>i:
		menor = i
	if maior<i:
		maior = i
print(menor)
print(maior)
print(soma)
