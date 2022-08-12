# def saudacao(saudacao, nome):
#     return (saudacao +', ' + nome + ' !!!')
# var = saudacao('bom dia', 'emanuel')
# print (var)

# def soma3(n1,n2,n3):
#     return print(n1+n2+n3)
# soma3(3,2,5)

# def percentual(n1, percentual):
#     return print('O aumento foi de: ', n1 * percentual/100)
# percentual(1200, 2)

def fizzBuzz(n1):
    # print(n1/3)
    if n1%3 == 0:
        return print('fizz')
    elif n1%5 == 0:
        return print('buzz')
    elif n1%3 == 0 and n1%5 == 0:
        return print('fizz buzz')
    else:
        return print(n1)
fizzBuzz(15)