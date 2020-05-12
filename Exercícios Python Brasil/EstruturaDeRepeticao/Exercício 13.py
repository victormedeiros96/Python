base = float(input("Base: "))
expoente = int(input("Expoente: "))
potencia = 1
for i in range(expoente):
	potencia *= base
print(potencia)
