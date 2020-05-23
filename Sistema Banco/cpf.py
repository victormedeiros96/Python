class CPF:
	def __init__(self,cpf):
		self.__cpf = self.__remover_caracteres_especiais(cpf)
	def __str__(self):
		return self.__cpf
	def valido(self):
		if len(self.__cpf)!=11:
			return False
		if not(self.__verificar_digito_repetido()):
			return False
		if not(self.__validar_primeiro_digito()):
			return False
		if not(self.__validar_segundo_digito()):
			return False
		return True
	def __remover_caracteres_especiais(self,cpf):
		if "." in cpf:
			cpf = cpf.replace(".","")
		if "-" in cpf:
			cpf = cpf.replace("-","")
		return cpf
	def __verificar_digito_repetido(self):
		if self.__cpf in ("1"*11,"2"*11,"3"*11,"4"*11,"5"*11,"6"*11,"7"*11,"8"*11,"9"*11):
			return False
		return True
	def __validar_primeiro_digito(self):
		produto = 0
		for i in range(10,1,-1):
			produto += int(self.__cpf[10-i])*i
		produto*=10
		if (produto%11)==int(self.__cpf[9]):
			return True
		else:
			return False
	def __validar_segundo_digito(self):
		produto = 0
		for i in range(11,1,-1):
			produto += int(self.__cpf[11-i])*i
		produto*=10
		if (produto%11)==int(self.__cpf[10]):
			return True
		else:
			return False
