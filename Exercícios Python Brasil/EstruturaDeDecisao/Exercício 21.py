valor = int(input("Valor mínimo de saque: R$ 10.00. Valor máximo R$ 600.00.\nInforme o valor que deseja sacar: "))
if valor<10 or valor>600:
	print('Valor incorreto.');exit()
notas = [0,0,0,0,0] # referencia [1,5,10,50,100]
while valor:
	if valor>=100:
		valor -= 100
		notas[4] +=1
	elif valor>=50:
		valor -= 50
		notas[3] +=1
	elif valor>=10:
		valor -= 10
		notas[2] +=1
	elif valor>=5:
		valor -= 5
		notas[1] +=1
	elif valor>=1:
		valor -= 1
		notas[0] +=1
print(f'''Notas de 100: {notas[4]}
Notas de 50: {notas[3]}
Notas de 10: {notas[2]}
Notas de 5: {notas[1]}
Notas de 1: {notas[0]}''')
