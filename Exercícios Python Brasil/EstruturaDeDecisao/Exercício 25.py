print('Responda \'1\' para sim ou \'0\' para não, para as seguintes perguntas')
r1 = input("Telefonou para a vítima?")
r2 = input("Esteve no local do crime?")
r3 = input("Mora perto da vítima?")
r4 = input("Devia para a vítima?")
r5 = input("Já trabalhou com a vítima?")
resultado = r1+r2+r3+r4+r5
if resultado==5:
	print('Assassino')
elif resultado>=3:
	print('Cúmplice')
elif resultado==2:
	print('Suspeito')
else:
	print('Inocente')
