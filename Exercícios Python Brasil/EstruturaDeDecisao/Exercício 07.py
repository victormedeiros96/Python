n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
n3 = float(input("Digite o número 3: "))
if (n1>=n2)and(n1>=n3):
	print(f"Maior: {n1}")
	if n2>=n3:
		print(f"Menor: {n3}")
	else:
		print(f"Menor: {n2}")
elif (n2>=n1)and(n2>=n3):
	print(f"Maior: {n2}")
	if n1>=n3:
		print(f"Menor: {n3}")
	else:
		print(f"Menor: {n1}")
elif (n3>=n1)and(n3>=n2):
	print(f"Maior: {n3}")
	if n1>=n2:
		print(f"Menor: {n2}")
	else:
		print(f"Menor: {n1}")
