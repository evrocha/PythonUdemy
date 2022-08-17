# exercicio 01

def funcao2():
    return ('valor')

def funcao1(funcao2):
    return funcao2()

x =funcao1(funcao2)
print(x)

# exercicio 02

def funcao02():
    return ('valor2')

def funcao01(funcao02, *args, **kwargs):  ##meste
    return funcao02(*args, **kwargs)

