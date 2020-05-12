Cidades = [{"codigo":987,"veiculos":654,"acidentes":321}, # Cidade 1
{"codigo":876,"veiculos":543,"acidentes":219}, # Cidade 2
{"codigo":765,"veiculos":432,"acidentes":198}, # Cidade 3
{"codigo":654,"veiculos":321,"acidentes":987}, # Cidade 4
{"codigo":543,"veiculos":219,"acidentes":876}  # Cidade 5
]
# Calculo da média de veículos
totalVeiculos = 0 # Para calcular a média, vamos somar todos e depois dividir
for cidade in Cidades:
	totalVeiculos += cidade["veiculos"]
mediaVeiculos = totalVeiculos/len(Cidades)
# Cálculo das cidades com mais e menos acidentes
menor_indice_acidentes = 0
maior_indice_acidentes = 0
for i in range(len(Cidades)):
	if Cidades[menor_indice_acidentes]["acidentes"] > Cidades[i]["acidentes"]:
		menor_indice_acidentes = i
	if Cidades[maior_indice_acidentes]["acidentes"] < Cidades[i]["acidentes"]:
		maior_indice_acidentes = i
# Cálculo da média de acidentes em cidades com menos de 2000 habitantes
totalAcidentes = 0;cont=0
for cidade in Cidades:
	if cidade["veiculos"]<2000:
		totalAcidentes += cidade["acidentes"]
		cont+=1
mediaAcidentes = totalAcidentes/cont
print(f"Maior índice de acidentes ocorreu na cidade {Cidades[maior_indice_acidentes]['codigo']} com {Cidades[maior_indice_acidentes]['acidentes']} acidentes.")
print(f"Menor índice de acidentes ocorreu na cidade {Cidades[menor_indice_acidentes]['codigo']} com {Cidades[menor_indice_acidentes]['acidentes']} acidentes.")
print(f"Média de veículos nas 5 cidades analisadas: {mediaVeiculos:g}.")
print(f"Média de acidentes nas cidades com mais de 2000 habitantes: {mediaAcidentes:g}.")
