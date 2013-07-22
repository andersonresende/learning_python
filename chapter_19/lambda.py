#lambda e para ser usada em casos simples.
#lambda aceita argumentos default. lambda nao necessita de argumentos.
#lambda e uma expressao e nao um bloco de codigo.


#expressao ternaria em lambda
fun = lambda x,y: x if x > y else y

print fun(4,5)