class Retangulo:
	def __init__(self,ladoA=None,ladoB=None):
		if ladoA:
			self._ladoA = ladoA
		else:
			self._ladoA = 0
		if ladoB:
			self._ladoB = ladoB
		else:
			self._ladoB = 0
	def mudarLados(self,novoLadoA,novoLadoB):
		self._ladoA,self._ladoB = novoLadoA,novoLadoB
	def area(self):
		return self._ladoA*self._ladoB
	def perimetro(self):
		return 2*(self._ladoA+self._ladoB)
	@property
	def ladoA(self):
		return self._ladoA
	@property
	def ladoB(self):
		return self._ladoB
	@property
	def lados(self):
		return (self._ladoA,self._ladoB)
r1 = Retangulo()
r2 = Retangulo(2,3)
print(r1.ladoA,r2.ladoB)
print(r1.area(),r2.area())
r1.mudarLados(4,5)
print(r1.lados,r2.lados)
print(r1.area(),r2.area())
