#def cria um objeto funcao com o nome a ela atribuido, no momento que a importamos.
#ele criar a funcao em tempo de execucao e nao compilacao, tudo em python e criado no momento
#que e invocado. Voce pode durante a execucao do sistema criar novas funcoes.Pq funcoes em python
# sao objetos, diferentemente de java. Entao criar uma funcao e como 'instanciar um objeto'.
# essa e a logica de que em python tudo sao objetos. Se python criace funcoes nao como objetos e em tempo
#de compilacao, duas funcoes com o mesmo nome dariam erro, mesmo que envoltas em uma condicao if
#para um ou outra.
# funcoes em python nao sao typadas nem nos parametros, nem nos retornos.
#polimorfismo = assumir comportamentos variados dependendo do objeto ex: *
#assim funcoes em python nunca podem dar erro de compilacao, pq nao sabemos oque elas recebem
#ou oque elas retornam.

input = raw_input('input:')
if input:
	def fun():
		print input
else:
	def fun():
		print 'no input'
fun()