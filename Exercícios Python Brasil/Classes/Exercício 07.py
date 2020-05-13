class Tamagoshi:
	def __init__(self,nome=None,fome=0,saude=100,idade=0):
		self._nome = nome
		self._fome = fome
		self._saude = saude
		self._idade = idade
		self._humor = self.saude-self.fome
		print("Nasceu.")
	@property
	def nome(self):
		return self._nome
	@property
	def fome(self):
		return self._fome
	@property
	def saude(self):
		return self._saude
	@property
	def idade(self):
		return self._idade
	def __str__(self):
		return f"{self.nome} -- {self.fome} -- {self.saude} -- {self.idade}\nHumor {self.humor}"
	@nome.setter
	def nome(self,novoNome):
		self._nome = novoNome
	@fome.setter
	def fome(self,fomeAtual):
		self._fome = fomeAtual
	@saude.setter
	def saude(self,saudeAtual):
		self._saude = saudeAtual
	@idade.setter
	def idade(self,idadeAtual):
		self._idade = idadeAtual
	@property
	def humor(self):
		return self._humor
	

bichinho = Tamagoshi("Meu bichinho",0,100,0)
print(bichinho)
