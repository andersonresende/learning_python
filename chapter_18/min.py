def min1(*args):
	'''
	Retorna o menor valor, passado em uma tupla.
	'''
	res = args[0]
	for arg in args[1:]: 
		if arg < res: res = arg
	return res

print min1(10,2,3,4)

def min2(first, *rest):
	'''
	Retorna o menor valor, recebendo um argumento inicial
	e outros em uma tupla.
	'''
	for arg in rest:
		if arg < first: first = arg
	return first

print min2('a','c','b')


def min3(*args):
	'''
	Recebe uma tupla e retorna o meno valor contido.
	'''
	tmp = list(args)
	tmp.sort() 
	return tmp[0]

print min3([1,2],[3,4],[0,1])

#em python tuplas sao imutaveis logo, nao podemos trocar objetos ou
#reordena-las.
#lista.sort() ordena a lista
#strip()-tirar retira espacos, split('b')-divisao quebra por argumento, ou espaco.