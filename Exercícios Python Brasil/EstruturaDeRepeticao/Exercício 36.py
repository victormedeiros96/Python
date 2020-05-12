n = int(input("Tabuada do: "))
a = int(input("Começar por: "))
b = int(input("Terminar em: "))
if a<b:
	for i in range(a,b+1):
		print(f"\t{n} x {i} = {n*i}")
else:
	print("Valores inválidos")
