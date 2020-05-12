# Utilizaremos a mesma ideia do exercício 37
maisAlto = {"codigo":0,"altura":0}
maisBaixo = {"codigo":0,"altura":1e3}
for i in range(10):
	codigo = int(input("Código do aluno: "))
	altura = float(input("Altura: "))
	if maisAlto["altura"]<altura:
		maisAlto["codigo"] = codigo
		maisAlto["altura"] = altura
	if maisBaixo["altura"]>altura:
		maisBaixo["codigo"] = codigo
		maisBaixo["altura"] = altura
print(maisBaixo)
print(maisAlto)
