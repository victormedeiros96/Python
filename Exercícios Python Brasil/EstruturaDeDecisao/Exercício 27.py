peso_morango = float(input("Peso em morangos: "))
peso_maca = float(input("Peso em maçãs: "))
if peso_morango<5:
	custo_morango = peso_morango*2.50
else:
	custo_morango = peso_morango*2.20
if peso_maca<5:
	custo_maca = peso_maca*1.80
else:
	custo_maca = peso_maca*1.50
custo = custo_maca+custo_morango
if (custo>25) or (peso_maca+peso_morango>8):
	custo = custo*.90
print(f"Custo total: R$ {custo}.")
