


def multi(arg1,arg2):
	'''
	Funcao polimorfica que faz operacoes diferentes
	dependendo dos argumentos passados.
	'''
	return arg1 * arg2

if __name__ == '__main__':
	#multiplica 2X2
	print multi(2,2)
	#duplica a string '2' 
	print multi('2',2) 
	#print multi('2','2') TypeError: multiplicacao de string X string
