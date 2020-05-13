class Bola:
	def __init__(self,color,circumference,material):
		self._color = color.lower()
		self._circumference = circumference
		self._material = material.lower()
	def trocaCor(self,newColor):
		self._color = newColor.lower()
	def mostraCor(self):
		print(self._color)

b = Bola("Azul",1.2,"borracha")
b.mostraCor()
