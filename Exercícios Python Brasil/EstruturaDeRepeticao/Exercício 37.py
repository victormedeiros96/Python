maisMagro = {"codigo":0,"peso":1e3,"altura":0}
maisGordo = {"codigo":0,"peso":-1e3,"altura":0}
maisAlto = {"codigo":0,"peso":0,"altura":0}
maisBaixo = {"codigo":0,"peso":0,"altura":1e3}
somaAlturas,somaPesos=0,0
cont = 0
while True:
	codigo = int(input("Código do cliente: "))
	if not codigo:
		break
	cont+=1
	peso = float(input("Peso: "))
	altura = float(input("Altura: "))
	somaAlturas+=altura
	somaPesos+=peso	
	if maisMagro["peso"]>peso:
		maisMagro["peso"] = peso
		maisMagro["codigo"] = codigo
		maisMagro["altura"] = altura
	if maisGordo["peso"]<peso:
		maisGordo["peso"] = peso
		maisGordo["codigo"] = codigo
		maisGordo["altura"] = altura
	if maisAlto["altura"]<altura:
		maisAlto["peso"] = peso
		maisAlto["codigo"] = codigo
		maisAlto["altura"] = altura
	if maisBaixo["altura"]>altura:
		maisBaixo["peso"] = peso
		maisBaixo["codigo"] = codigo
		maisBaixo["altura"] = altura
print(f"Peso médio: {somaPesos/cont:g}")
print(f"Altura média: {somaAlturas/cont:g}")
print(maisMagro)
print(maisGordo)
print(maisBaixo)
print(maisAlto)
