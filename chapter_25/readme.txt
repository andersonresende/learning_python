#General OOP ideas like inheritance and composition 
#apply to any application that can be decomposed into a set of objects.
#For example, in typical GUI systems, interfaces are written as collections of widgets—buttons,
#labels, and so on—which are all drawn when their container is drawn (composition). Moreover, 
#we may be able to write our own custom widgets—buttons with unique fonts, labels with new color schemes,
#and the like—which are specialized versions of more general interface devices (inheritance).


Classes em Python X Other languages
For example, as in C++, the class statement is Python’s main OOP tool, but unlike in C++, Python’s class is not a declaration. Like a def, a class statement is an object builder, and an implicit assignment—when run, it generates a class object and stores a reference to it in the name used in the header. Also like a def, a class statement is true executable code—your class doesn’t exist until Python reaches and runs the class statement that defines it (typically while importing the module it is coded in, but not before).

O codigo dentro de uma classe e executado quando ela e criada e nao quando e utilizada.
Assim ao importarmos um modulo que contenha classes, o codigo da classe e executado, pois nesse
momento o object classe e criado. Desta forma, nao e preciso esperar que um objeto seja instanciado
para aquela classe.
Ex:
module 1:
class teste():
	print 'module1'

module 2:
import mudule 1

ao executarmos o modulo 2 seria impresso 'module1'.


Metodo = funcoes das classes.
Funcoes = funcoes que nao pertencem a classes.


abstract superclass—a class that expects parts of its behavior to be
provided by its subclasses. If an expected method is not defined in a subclass, Python raises an undefined name exception when the inheritance search fails. Classes abstratas nao sao obrigatorias, elas sao muito mais um padrao, que vc deve utilizar quando outras classes precisarem de metodos em comum. Digamos que seu sistema,
exiba varias telas diferentes, e todas compartilhem obrigatoriamente para o bom funcionamento de metodos em comum, a ideia e organizar esses metodos em uma classe abstrata, e extendela nas outras classes, para que elas
implementem esses metodos. Assim quando alguem for criar uma nova tela vai saber da obrigatoriedade desses metodos. Se vc nao faz isso, nao herda dessa classe, vc teria que advinhar, ou esperar o sistema fahar em varios
momentos para advinhar quais metodos precisam ser implementados. As classes abstratas tambem podem prover partes de codigos que so fazem sentido se utilizados na subclasse com a implementacao dos metodos abstratos. Ex: um
metodo que chama outro abstrato, so funcionara se o outro for implementado. Entao nao e so pra que classes que
precisem de metodos em comum, saibam quais metodos implementar, mas tambem para que, as classes funcionem de
forma satisfatoria. Sem o pedaco de codigo e classe a implementar, vc teria que escrever cada classe indepentemente, com tudo isso, e teria que tratar ainda muitos erros no sistema.
ex:

#classe abstrata pois precisa da implmentacao de metodos na subclasse, compartilhando entre as classes
#metodos necessarios em todas e tambem partes de codigo ja prontas.
class Super:
	def delegate(self):
		#more code to be here
		self.action()
	def action(self):
		raise NotImplementedError('action must be defined!')