#namespace - o local onde um nome vive. exemplo nomes definidos dentro de uma funcao so existem
#dentro dela, e nao entram em conflito com nomes fora.
#local scope - functions, classes
#global scope - modules
#LEGB - ordem de procura por variavel, Local, Enclosed, Global, Builtins

X = 99

def func1():
	global X
	X = 88

def func2():
	global X
	X = 77

def func3():
	global Y
	Y = 5

if __name__ == '__main__':
	func1()
	print X
	func2()
	print X
	func3()
	print Y