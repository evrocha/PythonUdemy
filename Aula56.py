# o * antes de passar um parametro da funcao diz que esta funcao tem parametros nao limitados
def  funcao(*args, **kwargs): ## key word arguments (**) 
    print(args)
    
    nome = kwargs.get('nome')
    print(nome)
    
    sobrenome = kwargs.get('sobrenome')
    print(sobrenome) 

    idade = kwargs.get('idade') # caso passe uma kwarg q nao exista, vai ter NONE  

lista = [1, 2, 3, 4]
funcao(*lista) # aqui, o * faz com que a lista seja "desempacotada", ou seja, retorna os valores fora da lista

lista2 = [5,6,7,8]

funcao(*lista, *lista2) # vai ter um retorno como se nao houvesse duas listas juntas, j´pa que há o DESEMPACOTAMENTO

funcao(*lista, *lista2,nome= 'Emanuel', sobrenome = 'rocha') # kwargs. nao tem o retorno na funcao, ja q nao é chamado
