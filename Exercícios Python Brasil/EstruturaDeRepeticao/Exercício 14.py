n = list()
for i in range(10):
	n.append(int(input( f"Numero {i+1}: ")))
contPares = 0
for i in range(10):
	if not(n[i]%2): # resto da divisao com dois vai dar zero se for par e qualquer outra coisa se for impar
		contPares+=1# Se for par, o not vai fazer virar True, e entra no if, se for impar n entra
contImpares = 10-contPares
print(f"Pares: {contPares}\nImpares: {contImpares}")
