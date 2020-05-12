n = list()
for i in range(5):
	n.append(float(input("Numero: "))) # Adiciona na lista N os valores convertidos para float
# Poderia ser utilizado o método max, porém, iremos utilizar comparação
maior = n[0]
for i in range(1,5):
	if maior<n[i]:
		maior = n[i]
print(f"O maior número é {maior:g}.")
# # Extra
#
# print(f"Maior {max(n):g}")
