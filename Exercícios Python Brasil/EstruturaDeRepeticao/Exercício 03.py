while True:
	nome = input("Nome: ")
	idade = int(input("Idade: "))
	salario = input("Salário: ")
	sexo = input("Sexo (m ou f): ").lower()
	estado_civil = input("Estado Civil (s,c,v,ou d): ").lower()
	if len(nome)>3:
		if idade in range(151):
			if int(salario)>0:
				if sexo in ('m','f'):
					if estado_civil in ('s','c','v','d'):
						exit()
					else:
						print('Estado Civil inválido');continue
				print('Sexo inválido');continue
			print('Salário inválido');continue
		print('Idade inválida');continue
	print('Nome deve ter mais de 3 caracteres');continue
