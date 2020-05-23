from conectarAoBancoDeDados import ConectarBandoDeDados
from numpy import random
class Conta:
	def __init__(self,titular,agencia,senha,numero_conta=None,saldo=0):
		self.__titular = titular
		self.__agencia = agencia
		self.__saldo = saldo
		self.__senha = senha
		self.limite_negativo = 0
		if numero_conta==None:
			self.__numero_conta=Conta.__gerar_numero_conta()
			self.__adicionar_ao_banco_de_dados()
		else:
			self.__numero_conta = numero_conta
	def __str__(self):
		retorno = f"""Titular: {self.__titular}
		RG: {self.__titular.rg}
		CPF: {self.__titular.cpf.__str__()}
		Agencia: {self.__agencia}
		Conta: {self.__numero_conta}
		Saldo: R$ {self.__saldo:.2f}
		"""
		return retorno
	@staticmethod
	def __gerar_numero_conta():
		conectar = ConectarBandoDeDados()
		contas = conectar.ler_Contas_Existentes()
		print(contas)
		if contas:
			a = contas[0]
			while a in contas:
				a = (list(random.randint(0,9,10).astype("str")))
				a = "".join(a)
		else:
			a = (list(random.randint(0,9,10).astype("str")))
			a = "".join(a)
		return a
	def __adicionar_ao_banco_de_dados(self):
		conectar = ConectarBandoDeDados()
		tupla = ((self.__titular.nome,self.__titular.rg,self.__titular.cpf.__str__(),self.__agencia,self.__numero_conta,0,self.__senha))
		conectar.inserir(tupla)
	@property
	def saldo(self):
		return self.__saldo
	@property
	def titular(self):
		return self.__titular
	@property
	def agencia(self):
		return self.__agencia
	@property
	def numero_conta(self):
		return self.__numero_conta
	def depositar(self,valor):
		try:
			self.__saldo+=valor
			conectar = ConectarBandoDeDados()
			conectar.atualizar_conta(self.numero_conta,self.__saldo)
			return True
		except Exception as e:
			print(e)
			return False
	def sacar(self,valor):
		try:
			if self.__saldo>=valor:
				self.__saldo-=valor
				conectar = ConectarBandoDeDados()
				conectar.atualizar_conta(self.numero_conta,self.__saldo)
				return True
			else:
				print("Saldo insuficiente")
				return False
		except Exception as e:
			print(e)
			return False
	def transferir(self,destino):
		cpf = destino.cpf
		if cpf.valido():
			conta = destino.conta
		else:
			return False
