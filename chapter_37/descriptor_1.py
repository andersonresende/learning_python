'''
### Descriptor nao generico e externo ###
Exemplificamos um descriptor nao generico pois utiliza
a variavel da instacia pra atribuicao. Podemos fazer um
descriptor generico se nao trabalharmos com variaveis de
instancia e usarmos a de classe, utilizando um descriptor
que recebe argumentos ou nao.
'''

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

import pdb
pdb.set_trace()
p1 = Person('Anderson')
p2 = Person('Renato')
print p1.name
print p2.name
p1.name = 'Anderson2'
del p1.name
#print p1._name #erro pois _name foi deletado


