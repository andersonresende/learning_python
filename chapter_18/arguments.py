'''
Python trabalha com ponteiros que fazem a ligacao entre nomes e objetos.
Ao vc atribuir um valor(novo objeto), a um nome(variavel) voce esta fazendo
com que o nome aponte(referencie) o novo objeto e perca a referencia anterior.

	a = 1
	b = 2

	b = a
	a = 3
	print b #imprime 1

Da mesma forma:
	def f(a):
		a = []

	b = [1]
	f(b)
	print b #imprime [1]

Existem objetos mutaveis(listas,dicionarios) e objetos imutaveis(1,"abc").
Desta mesma forma, se vc altera uma lista que esta contida em outra, 
Ao acessa-la fora da lista ela tera sido alterada. Por que cada posicao
em uma lista, tupla ou dict aponta pra um objeto.
	
	l = [1,2]
	def ft(t):
	 	return t,1

	l1 = ft(l) 
	l[0] = 2
	print l1 #imprime ([2,2],1)
'''