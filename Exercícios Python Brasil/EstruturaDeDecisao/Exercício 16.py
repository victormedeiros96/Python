a = float(input("Valor de A: "))
if a==0:
	print("Não é uma equação do segundo grau.")
	exit()
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))
delta = b**2-4*a*c
if delta<0:
	print("Delta negativo, não existem raizes reais.")
	exit()
elif delta==0:
	print(f"Raizes duplas em {(-b/2/a):g}.")
else:
	print(f"Raizes {(-b+delta**0.5)/2/a:g} e {(-b-delta**0.5)/2/a:g}.")
