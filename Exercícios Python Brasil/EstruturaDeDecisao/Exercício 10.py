resposta = input("Em que turno você estuda? (M-matutino,V-Vespertino,N-Noturno) ").upper()
if resposta=="M":
	print("Bom dia!!")
elif resposta=="V":
	print("Boa tarde!!")
elif resposta=="N":
	print("Boa noite!!")
else:
	print("Valor inválido")
'''
# EXTRA
# Poderia utilizar um dicionário para facilitar esse processo:
exemplo = {"M":"Bom dia!!","V":"Boa tarde!!","N":"Boa noite!!"}
try:
	auxiliar = exemplo[resposta]
	print(auxiliar)
except KeyError:
	print("Valor inválido")
'''
