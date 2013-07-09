class PropSquare(object):
	def __init__(self, start):
		self.value = start

	@property
	def X(self):
		"documentacao X"
		return self.value ** 2
	@X.setter
	def X(self, value):
		self.value = value
	@X.deleter
	def X(self):
		del self.value

p = PropSquare(3)
p.X = 4
print p.X, p.value
print(PropSquare.X.__doc__)


