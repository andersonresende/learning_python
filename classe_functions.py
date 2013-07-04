

class Numero(object):
	'''
	Classe utilizada para testar os comportamentos dos
	metodos de classe, estaticos e normais. 1. Apenas
	os metodos de classe tem acesso a variaveis de classe.
	2. Nenhum dos metodos pode ser transferido para outra
	variavel.
	'''

	a = 2

	@classmethod
	def menos(cls):
		print cls.a

	@staticmethod
	def mais():
		print a

	def meio():
		print a


if __name__ == '__main__':
	try:
		print '-'*70
		print 'Testando se o METODO DE CLASSE menos\ntem acesso a variaveis de classe:'
		Numero.menos()
	except:
		print 'Falha ao tentar acessar!'
	try:
		print '-'*70
		print 'Testando se o METODO ESTATICO mais\ntem acesso a variaveis de classe:'
		Numero.mais()
	except:
		print 'Falha ao tentar acessar!'
	try:
		print '-'*70
		print 'Testando se o METODO NORMAL meio\ntem acesso a variaveis de classe:'
		Numero.meio()
	except:
		print 'Falha ao tentar acessar!'
