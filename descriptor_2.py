class DescSquare(object):
	def __init__(self, value):
		self.value = value
	def __get__(self, instance, owner):
		return self.value ** 2
	def __set__(self, instance, value):
		self.value = value


class Client(object):
	X = DescSquare(3)


c1 = Client()
print c1.X
c1.X = 5
print c1.X
#Nao da o resultado esperado, a composicao tem de ser feita diretamente na classe e nao no objeto.
c1.Y = DescSquare(10)
print c1.Y