dia = int(input("Dia da semana (1-7) : "))
if dia==1:
	aux = "Domingo"
elif dia==2:
	aux = "Segunda"
elif dia==3:
	aux = "Terça"
elif dia==4:
	aux = "Quarta"
elif dia==5:
	aux = "Quinta"
elif dia==6:
	aux = "Sexta"
elif dia==7:
	aux = "Sábado"
else:
	aux = "Valor Inválido"
print(aux)
'''
# EXTRA
# DE FORMA MAIS PYTHONICA, PODERIA SER FEITO ASSIM:
dias = {1:'Domingo',2:'Segunda',3:'Terça',4:'Quarta',5:'Quinta',6:'Sexta',7:'Sábado'}
try:
	print(dias[dia])
except KeyError:
	print('Valor Inválido')
'''
