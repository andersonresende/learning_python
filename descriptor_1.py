#essa classe pode estar dentro da classe Person tambem.
class Name(object):
	'''name descriptors docs'''
	def __get__(self, instance, owner):
		print 'fetch'
		return instance._name
	def __set__(self, instance, value):
		print 'change'
		instance._name = value
	def __delete__(self, instance):
		print 'delete'
		del instance._name


class Person(object):
	def __init__(self, name):
		self._name = name
	name = Name()


p1 = Person('Anderson')
p2 = Person('Renato')
print p1.name
print p2.name
p1.name = 'Anderson2'
del p1.name
#print p1._name #erro pois _name foi deletado
