class Pessoa:
	def __init__(self,nome="",idade=0,peso=0,altura=0):
		self._nome = nome
		self._idade = idade
		# Idade em anos
		self._peso = peso
		# Peso em kg
		self._altura = altura
		# Altura em m
	def envelhecer(self,anos):
		if self._idade<21:
			self._altura += anos*.005
		self._idade += anos
	def engordar(self,peso):
		self._peso += peso
	def emagrecer(self,peso):
		self._peso -= peso
	def crescer(self,altura):
		self._altura += altura
	def __str__(self):
		return f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}"
	@property
	def nome(self):
		return self._nome
	@property
	def peso(self):
		return self._peso
	@property
	def altura(self):
		return self._altura
	@property
	def idade(self):
		return self._idade
victor = Pessoa("Victor",18,68,1.70)
print(victor)
victor.engordar(2)
print(victor)
victor.emagrecer(1)
print(victor)
victor.crescer(0.05)
print(victor)
victor.envelhecer(2)
print(victor)
