#funcoes lambdas apenas utilizam argumentos de outra funcao acima
#se definirem no parametro como default ou o valor estiver dentro da funcao lambda
#e nao nos seus parametros.
# def func_teste():
# 	x = 10
# 	#retorna uma lambda que precisa de dois arguementos, ignora o x da funcao superior.
# 	return lambda x,i: x * i
# 	#retorna uma funcao lambda que usa o x da superior.
# 	return lambda i: x * i
# 	#retorna uma funcao lambda que usa o x da superior como valor default.
# 	return lambda x=x,i: x * i


def func1():
	'''
	Uma funcao que retorna uma segunda funcao,
	que utiliza um valor definido na primeira em
	seu escopo.
	'''
	x = 10
	def func2(n):
		return n * x
	return func2
    
def make_func():
	'''
    Uma funcao que retorna uma lista com varias funcoes
    lambda. No entanto, todas usam o ultimo valor de x
    em seu corpo.
	'''
	list_fun = []
	for x in range(5):
		list_fun.append(lambda i: i * x)
	return list_fun


if __name__ == '__main__':
	f = func1()
	print f
	print f(3)

	list_fun = make_func()
	fun1 = list_fun[1]
	fun2 = list_fun[2]
	print fun1(2)
	print fun2(2)


