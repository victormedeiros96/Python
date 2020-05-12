ano_inicial = 1995
salario_inicial = 1000
taxa_inicial = 0.015
taxa = taxa_inicial
salario = salario_inicial
for i in range(ano_inicial+1,2021):
	salario = salario*(taxa+1)
	print(salario,taxa)
	taxa *= 2
print(f"Salário atual: {salario:g}")
