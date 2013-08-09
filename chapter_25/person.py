class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name 
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))
	def __str__(self):
		return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
	def __init__(self, name, pay):
		#chamando da super-classe preservamos uma possivel logica existente na super-classe. 
		Person.__init__(self, name, 'mgr', pay)
	def giveRaise(self, percent, bonus=.10):
		Person.giveRaise(self, percent + bonus)


#tambem poderiamos usar delegation-composite ao inves de heranca, mas tudo parece fazer menos sentido, semanticamente
#em uma delegacao eu nao posso chamar diretamento os metodos da classe delegada, no objeto da classe que usa, eu teria que chamar apartir da
#variavel que o objeto esta, ou sobrescrever os metodos, mesmo que nao fosse necessario fazer uma alteracao, so
#pra chamar diretamente.

if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	print(bob)
	print(sue)
	print(bob.lastName(), sue.lastName())
	sue.giveRaise(.10)
	print(sue)
	tom = Manager('Tom Jones', 50000)
	tom.giveRaise(.10)
	print(tom.lastName())
	print(tom)

	#usando o shelve, um banco nao-relacional
	import shelve
	db = shelve.open('persondb')
	db['name2'] = 'Anderson2'
	db.close()
	db = shelve.open('persondb')
	print len(db)
	print db['name2']


#se vc adicona mais um parametro em um metodo, nao e melhor criar um novo??
#pq esse novo argumento provavelmente vai modificar todo o corpo do metodo.
#agora se ele e apenas um incremento em outro argumento, podemos pensar em
#outra maneira.
# o self em um metodo permite que nos possamos chamar um metodo de objeto,
#atraves de uma classe. ex: Person.giveRaise(self, percent + bonus)
#isso e muito importante quando queremos customizar metodos nas subclasses.
#e preciso saber qual a melhor forma de fazer dependendo do que queremos.