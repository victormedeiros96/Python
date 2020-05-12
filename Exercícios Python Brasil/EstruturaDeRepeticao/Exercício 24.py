somador_notas = 0
contador = 0
while True:
	aux = float(input("Adicione uma nota (-1 para parar): "))
	if aux==-1:
		break
	else:
		somador_notas+=aux
		contador+=1
print(f"A média é {somador_notas/contador:g}.")
