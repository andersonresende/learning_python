class Person(object):
	def __init__(self,name):
		self._name = name
	def get_name(self):
		print 'fetch'
		return self._name
	def set_name(self,name):
		print 'assigment'
		self._name = name
	def del_name(self):
		print 'delete'
		del self._name

	name = property(get_name,set_name,del_name,"none docs")

person = Person('Anderson')
print person.name
print person._name


#Sera que essa dificuldade em criar gets e sets tem haver com a verificacao da linguagem de script?
#a variavel que vai receber o valor final tem que ser diferente da variavel que recebe o valor.
#pq so assim nao acontece a recursividade, tanto no get como no set.



# class Person(object):
# 	def __init__(self, name):
# 		self._name = name 
# 	def getName(self):
# 		print('fetch...')
# 		return self._name
# 	def setName(self, value): 
# 		print('change...')
# 		self._name = value
# 	def delName(self):
# 		print('remove...')
# 		del self._name
# 	name = property(getName, setName, delName, "name property docs")
# bob = Person('Bob Smith') 
# print(bob.name)
# bob.name = 'Robert Smith' 
# print(bob.name)
# del bob.name
# print('-'*20)
# sue = Person('Sue Jones') 
# print(sue.name) 
# print(Person.name.__doc__)
# # bob has a managed attribute 