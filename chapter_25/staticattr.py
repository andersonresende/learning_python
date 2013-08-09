class MixedNames: 
	data = 'spam'
 	def __init__(self, value):
 		self.data = value

 	def printer(self):
 		print self.data
m1 = MixedNames(1)

print m1.data
#quando possuimos dois atributos, um statico e outro de instancia, com o mesmo nome, precisamos acessar
# o statico apartir da classe, pois se tentarmos no objeto, ele sempre tras o de instancia. Agora se houvesse
#apenas um dos dois ele sempre conseguiria diretamente do objeto.
print m1.__class__.data

#ao alterarmos um atributo statico na classe, ele e alterado em todos os objetos.Ja se alterarmos
#no objeto, ele mexe apenas no objeto alterado.

#formas de chamar um metodo

m1.printer()
#e importante passar o self == objeto como argumento, se ele for um metodo que depende da instancia.
MixedNames.printer(m1)

#se vc construir uma classe fazendo com que os atributos e seus tipos correspondam a seus metodos e seus tipos
#tudo faz muito sentido em python... Criar metodos de instancia que usam self, so fazem sentido se vc tiver um
#um construtor pq nele vc vai carregar os atributos, sem construtor os metodos podem simplismente falhar.
#ja para metodos estaticos, faz sentido tambem ter os atributos de forma statica, pq nao existe dependencia
# do construtor do objeto. Logo nao devemos definir atrr staticos dentro do construtor.


class B:
	def delegate(self):
		print self.a

class A(B):
	def __init__(self):
		self.a = 30
B().delegate() #nao funciona pois o attr a nao foi definido
A().delegate() #funciona pq o self==objeto passado no metodo da super-classe e a instancia de A 
# que possui o atributo a no seu objeto. 