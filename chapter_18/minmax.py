'''
Este modulo apresenta o uso de funcoes genericas.
Com estas funcoes podemos fazer coisas magicas, como
passar funcoes dentro de funcoes e valores indefinidos.
Desta forma ao inves de fazer varias funcoes completas,
podemos economizar varias linhas de codigo fazendo apenas
uma generica que recebe as outras mais simples.
'''

'''Funcao comparando valores'''
def minmax(test, *args):
	res = args[0]
	for arg in args[1:]:
		if test(arg, res):
			res = arg 
	return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y
print minmax(lessthan, 4, 2, 1, 5, 6, 3)
print minmax(grtrthan, 4, 2, 1, 5, 6, 3)

'''Funcao condicionais'''
def generic_assert(test, *args):
	lista = args
	nova_lista = []
	for a in args:
		if test(a):
			nova_lista.append(a)
	return nova_lista

def par(a):
	if not a%2: return True
	return False

def impar(a):
	if not a%2: return False
	return True

def mult_(m,a):
	if not a%m: return True
	return False

def contains_(s,a):
	if s in a: return True
	return False

print generic_assert(par,1,4,5,6,2,3)

'''Funcoes condicionais que recebem chaves'''
def generic_key(func, key, *args):
	lista = []
	for a in args:
		if func(key,a):
			lista.append(a)
	return lista

print generic_key(mult_,3,5,6,8,9,10)
print generic_key(contains_,'a','anderson','bola','gato','uol','bol')

'''Funcao extra'''
def intersect(*args):
	lista = args
	res = []
	for x in lista[0]:
		for other in lista[1:]:
			if x not in other:
				break
			else:
				res.append(x)
	return res

print intersect([1,2,3,4],[1,2,5,6],[3,4,6,1])


#int object is not iterable. 
#agora eu posso iterar por uma lista vazia. Nao vai dar erro. [a for a in []]