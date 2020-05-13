def lerCPF():
	cpf = input("CPF: ")
	return cpf
def removerCaracteresEspeciais(cpf):
	if "." in cpf:
		cpf = cpf.replace(".","")
	if "-" in cpf:
		cpf = cpf.replace("-","")
	return cpf
def validarPrimeiroDigito(cpf):
	cpf = removerCaracteresEspeciais(cpf)
	produto = 0
	for i in range(10,1,-1):
		produto += i* int(cpf[10-i])
	produto *= 10
	resto = produto%11
	if resto==int(cpf[-2]):
		return True
	else:
		return False
def validarDigitosRepetidos(cpf):
	cpf = removerCaracteresEspeciais(cpf)
	primeiroDigito = cpf[0]
	for digito in cpf:
		if primeiroDigito!=digito:
			return True
	return False
def main():
	print("Validador de CPF.")
	cpf = lerCPF()
	if (validarDigitosRepetidos(cpf))and(validarPrimeiroDigito(cpf)):
		print("CPF válido")
	else:
		print("CPF inválido")
	
	
if __name__=="__main__":
	main()
