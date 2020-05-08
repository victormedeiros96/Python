n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1+n2)/2
conceito,aprovado = "",""
if media<4:
	conceito = "E"
	aprovado = "Reprovado"
elif media<6:
	conceito = "D"
	aprovado = "Reprovado"
elif media<7.5:
	conceito = "C"
	aprovado = "Aprovado"
elif media<9:
	conceito = "B"
	aprovado = "Aprovado"
elif media<=10:
	conceito = "A"
	aprovado = "Aprovado"
print(f'''
Notas {n1}  {n2}
Média {media}
Conceito {conceito} -- {aprovado}
''')
