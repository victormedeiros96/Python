data = input("Digite uma data no formato dd/mm/aaaa: ")
dia = int(data[0:2]);mes = int(data[3:5]);ano = int(data[6:])
if mes>1 and mes<13:
	if dia<=31 and dia>0:
		if mes == 2:
			if not((ano%4==0) and not((ano%400) and not(ano%100))):
				if dia>28:
					print("Data inválida");exit()
			else:
				if dia>29:
					print("Data inválida");exit()
		elif mes in (4,6,9,11):
			if dia>30:
				print("Data inválida");exit()
	else:
		print("Data inválida");exit()
print("Data Válida")
