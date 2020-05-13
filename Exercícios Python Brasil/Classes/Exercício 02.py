class Quadrado:
	def __init__(self,lado=None):
		if lado:
			self._lado = lado
		else:
			self._lado = 0
	def mudarLado(self,novoLado):
		self._lado = novoLado
	def area(self):
		return self._lado**2
	@property
	def lado(self):
		return self._lado
q1 = Quadrado()
q2 = Quadrado(5)
print(q1.lado,q2.lado)
print(q1.area(),q2.area())
q1.mudarLado(4)
print(q1.lado,q2.lado)
print(q1.area(),q2.area())
