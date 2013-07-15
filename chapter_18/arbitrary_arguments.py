'''
Python possui formas de construir funcoes que nao determinam
a quantidade de argumentos que podem receber. Assim temos *args
e **kwargs. Tambem podemos usar essas notacoes para passar argumentos
em funcoes que ja tem um numero de parametros definidos. E como se
estivessemos passando os argumentos em uma lista ou dicionario, apenas
isso. Na falta de algum obrigatorio, ou adicao de algum outro a funcao
vai apresentar erros, como faria normalmente.
'''

'''Funcoes simples'''
def f(a,b,c=3):
	print a,b,c
args = [1,2,3]
f(*args)

def f2(a,b,c):
	print a,b,c
kwargs = {'a':1,'b':2,'c':3}
f2(**kwargs)

'''Funcoes avancadas'''
def tracer(func, *pargs, **kargs): 
	print('calling:', func.__name__) 
	return func(*pargs, **kargs)

def func(a, b, c, d): return a + b + c + d

print(tracer(func, 1, 2, c=3, d=4))

'''Funcoes avancadas 1'''
def add_one(func,*args,**kwargs):
	args = [a+1 for a in args]
	for k in kwargs:
		kwargs[k] = kwargs[k] +1
	return func(*args,**kwargs)

def multi(a,b): print a*b

add_one(multi,1,2)
add_one(multi,a=1,b=2)
add_one(multi,1,b=2)
