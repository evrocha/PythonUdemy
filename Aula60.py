## Expressões LAMBDA -> expressões anonimas

from cProfile import label
from traceback import print_tb


def funcao(n,n1):
    return print (n1 * n)
funcao(3,2)

a = lambda x,y: x*y # expressao LAMBDA
print(a(3,4)) 

lista = [
    ['P1', 13],
    ['P2', 4],
    ['P3', 3],
    ['P4', 2],
    ['P5', 36],
    ['P6', 113],
    ['P7', 76]
]

##
def func(item):
    return item[1]
lista.sort(key = func)
print(lista)

## usando o lambda
lista.sort(key = lambda item2:item2[1])
print(lista)