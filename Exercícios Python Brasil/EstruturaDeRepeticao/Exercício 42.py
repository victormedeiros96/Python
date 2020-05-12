dado = 0
contadorIntervalos = [0,0,0,0]
while dado>=0:
	dado = float(input('Digite um número positivo (para sair, digite um número negativo) : '))
	if (dado>=0) and (dado<=25):
		contadorIntervalos[0]+=1
	elif (dado>=26) and (dado<=50):
		contadorIntervalos[1]+=1
	elif (dado>=51) and (dado<=75):
		contadorIntervalos[2]+=1
	elif (dado>=76) and (dado<=100):
		contadorIntervalos[3]+=1
	elif dado<0:
		break
print(contadorIntervalos)
