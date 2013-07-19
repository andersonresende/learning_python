#nao mudar o tipo de uma variavel e uma boa pratica
#nao usar globais dentro de funcoes, pois pode criar dependencias.
#durante a recursao o escopo das funcoes e mantido, por isso funciona.
#recursao exige que vc crie uma funcao, enquanto procedural nao.
#vc nao pode alterar os valores de variaveis a partir de fora da funcao.

def mysum_1(l):
	'''	Soma uma lista recursivamente.'''
	if not l:
		return 0
	return l[0] + mysum(l[1:])

def mysum_2(l):
	'''	
	Soma uma lista recursivamente
	usando ternary expression.
	Funciona tambem com strings.
	'''
	return 0 if not l else l[0] + mysum(l[1:])

def mysum_3(l):
	'''	
	Soma uma lista com while.
	'''
	soma = 0
	while l:
		soma+=l[0]
		l = l[1:] #essa tecnica dispensa o uso de contadores.Muito bom!!!
	return soma

print mysum_3([1,2,3,4])

def sumtree(L):
	'''
	Funcao avancada de recursao que
	soma listas aninhadas. Essa soma
	so pode ser feita com recursao
	'''
	tot = 0
	for x in L:
		if not isinstance(x, list):
			tot += x
		else:
			tot += sumtree(x)
	return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))


