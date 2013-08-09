#Classes permitem,
#heranca  propriedades, caracteristicas em comum que podem ser reutilizadas, como uma heranca genetica rssrsr.
#composicao um objeto ser composto por outros objetos, trabalhando juntos.
#overloading - sobrecarga de operadores, metodo __add__
#os metodos str e add, ja existem por padrao em qualquer classe, ja o init nao, tem que ser definido.
#python e realmente foda, e possivel, apos criar uma classe adicionar novos metodos ou atributos nela.

class Teste:
	def __init__(self,a):
		self.value = a

	def __str__(self):
		return self.value

	def __add__(self, other):
		self.value = self.value+other

if __name__ == '__main__':
	teste = Teste('1')
	print teste
	teste+'13'
	print teste
	print teste.value

	#adicionando atributos e metodos apos a criacao da classe
	Teste.a = 'a'
	Teste.b = 'b'
	def fun(self):
		return 'fun'
	Teste.fun = fun

	teste2 = Teste(1)
	print teste2.a
	print teste2.b
	print teste2.fun()
