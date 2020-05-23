from cpf import CPF
class Destino:
	def __init__(self,nome,numero_conta,agencia,cpf):
		self.__cpf = CPF(cpf)
		self.__nome = nome.title()
		self.__conta = (agencia,numero_conta)
	@property
	def cpf(self):
		return self.__cpf
	@property
	def nome(self):
		return self.__nome
	@property
	def conta(self):
		return self.__conta

