'''
nos conseguimos acessar o atributo da classe via objeto, mas na hora que adicionamos um novo valor
e criado um com o mesmo nome no objeto, e nos passamos a manipula o do objeto. para acessar o da classe
devemos fazer via classe. Entao realmente ele e um atributo de classe... Pq se atribuirmos um valor a ele
na verdade estamos criando um novo atributo de instancia e a partir dae manipulando ele.
Atributos staticos devem ser declarados quando eles sao comuns a todos os objetos e se alterados em um objeto devem
alterar todos os objetos que o possuem, desta forma, a posicao estratefica deles tambem facilitam a heranca.
'''


class Person(object):
    #atributo de classe, so pode ser alterado via classemethod ou diretamente chamando a classe no objeto
    origin = 'Human'

    def __init__(self):
        #atributo de instancia, com o mesmo nome do de classe,tambem podemo cria-lo em tempo de execucao
        #self.origin = ###
        #sao dois atributos diferentes
        self.origin = 'ExtraHuman'

    @classmethod
    def get_class_origin(cls):
        return cls.origin


if __name__=='__main__':
    p1 = Person()
    print p1.origin
    print p1.get_class_origin()
    #altera o atributo de instancia
    p1.origin = 'Nova Origem'
    #altera o atributo de classe
    p1.__class__.origin = 'Super-Human'
    print p1.origin
    print p1.get_class_origin()





