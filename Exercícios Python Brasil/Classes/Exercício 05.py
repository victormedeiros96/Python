class ContaCorrente:
	def __init__(self,numeroDaConta,nomeCorrentista,saldo=0):
		self._numeroDaConta = numeroDaConta
		self._nomeCorrentista = nomeCorrentista.title()
		self._saldo = saldo
		print("Conta criada com sucesso!")
		print(self)
	def __str__(self):
		return f"Conta: {self.numeroDaConta} -- {self.nomeCorrentista}\nSaldo: R$ {self.saldo:.2f}"
	def deposito(self,valorDepositado):
		self._saldo += valorDepositado
		print(f"Depósito realizado no valor de R$ {valorDepositado:.2f}")
	def saque(self,valorSacado):
		if self.saldo>=valorSacado:
			self._saldo -= valorSacado
			print(f"Saque realizado no valor de R$ {valorSacado:.2f}")
		else:
			print("Saque não realizado. Saldo insuficiente.")
	@property
	def saldo(self):
		return self._saldo
	@property
	def numeroDaConta(self):
		return self._numeroDaConta
	@property
	def nomeCorrentista(self):
		return self._nomeCorrentista
	@nomeCorrentista.setter
	def nomeCorrentista(self,novoNome):
		print(f"Conta transferida do correntista {self.nomeCorrentista} para {novoNome}.")
		self._nomeCorrentista = novoNome.title()
		
conta = ContaCorrente(12345678,"Victor Israel Anchieta de Medeiros",600)
conta.saque(900)
print(conta)
conta.deposito(50)
print(conta)
conta.nomeCorrentista = "Sem nome"
print(conta)
