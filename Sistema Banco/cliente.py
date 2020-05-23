from cpf import CPF
class Cliente:
	def __init__(self,nome,rg,cpf,comprovantes):
		self.__nome = nome.title()
		self.__rg = rg
		self.__cpf = CPF(cpf)
		print(self.__cpf)
		if not(self.__cpf.valido()):
			print("CPF invalido, por favor, corrija.\n>>Cliente.cpf = \"cpf\"")
		if comprovantes:
			self.__comprovantes = True
		else:
			self.__comprovantes = False
	def __str__(self):
		return self.__nome
	@property
	def rg(self):
		return self.__rg
	@property
	def cpf(self):
		return self.__cpf
	@cpf.setter
	def cpf(self,novo_cpf):
		novo = CPF(novo_cpf)
		if novo.valido():
			self.__cpf = novo
		else:
			print("CPF invalido, por favor, insira um novo CPF.")
	@property
	def nome(self):
		return self.__nome
	@nome.setter
	def nome(self,novo_nome):
		self.__nome = novo_nome.title()
	@property
	def comprovantes_validos(self):
		return self.__comprovantes
