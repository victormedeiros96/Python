n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1+n2+n3)/3
if media==10:
	print(f"Aprovado com distinção.")
elif media>=7:
	print(f"Aprovado. Média {media}.")
else:
	print(f"Reprovado. Média {media}.")
