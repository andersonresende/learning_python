#new-style possuem __getattribute__ and __setattr__. 
#O __getattr__ e um metodo que pode ser implementado opcionalmente.
#O __getattribute__ e chamado pra qualquer atributo conhecido ou nao.
# Quado e desconhecido ele delega pra o __getattr__.
# Ou usamos o __dict__ para trabalhar com os atributos.
# Ou os metodos da super-classe para eveitar recusividade.
# o __getattribute__ tambem cobre os metodos. Ou melhor, qualquer chamada na classe ou objeto.
# A melhor pratica e para novos atributos mecher no __getattr__.
# So mecher no __getattribute__ para alterar os antigos.

#Em um for apenas precisamos separar os itens pro virgula sem ser necessario os colchetes.


class GetAttr:
	eggs = 88
	def __init__(self):
		self.spam = 77
	def __len__(self): 
		print('__len__: 42') 
		return 42
	def __getattr__(self, attr):
		if attr == '__str__':
			return lambda *args: '[Getattr str]'
		else:
			return lambda *args: None


class GetAttribute(object):
	eggs = 88
	def __init__(self):
		self.spam = 77
	def __len__(self):
		print('__len__: 42')
		return 42
	def __getattribute__(self, attr):
		print('getattribute: ' + attr)
		if attr == '__str__':
			return lambda *args: '[GetAttribute str]' 
		else:
			return lambda *args: None

	def soma(self):
		return 1


for Class in GetAttr, GetAttribute:
	print('\n' + Class.__name__.ljust(50, '='))
	X = Class()
	print X.soma()

	# X.eggs 
	# X.spam 
	# X.other
	# len(X)
	# try: 
	# 	X[0]
	# except:
	# 	print('fail []')
	# try:
	# 	X + 99
	# except:
	# 	print('fail +')

	# try:
	# 	X()
	# except:
	# 	print('fail ()')

	# X.__call__()
	# print(X.__str__())
	# print(X)