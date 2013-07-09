'''
### Descriptor interno e generico ###
Exemplificamos aqui a construcao de um descriptor
dentro de uma classe. Esse descriptor e generico, pois
nao acessa nenhum atributo da classe em que esta contido.
Apenas e utilizado por ela. Para as variaveis de instancia
acessarem os descriptors ou propertys a variavel do __init__
tem que ter o mesmo nome da que recebe o parametro.
'''


class Pessoa(object):
	def __init__(self, name):
		self.name = name

	class Desc(object):
		def __get__(self, instance, owner):
			return self.value
		def __set__(self, instance, value):
			self.value = value
	name = Desc()


p = Pessoa('anderson')
print p.name



