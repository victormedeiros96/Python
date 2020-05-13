class TV:
	def __init__(self,volume=0,canal=None):
		self._canal = None
		self._volume = volume
	@property
	def volume(self):
		return self._volume
	@property
	def canal(self):
		return self._canal
	def aumentarVolume(self):
		if self._volume<10:
			self._volume += 1
		print(f"Volume: {self._volume}")
	def diminuirVolume(self):
		if self._volume>0:
			self._volume -= 1
		print(f"Volume: {self._volume}")
	def mudarCanal(self,novoCanal):
		self._canal = novoCanal
	def __str__(self):
		return f"TV: canal {self._canal} -- volume {self._volume}"
televisor = TV()
print(televisor)
televisor.aumentarVolume()
print(televisor)
televisor.mudarCanal(5)
print(televisor)
print(televisor.canal,televisor.volume)
