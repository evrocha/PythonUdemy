from pessoa import Pessoa

p1 = Pessoa("Emanuel",  29)
# print(p1.comendo)
# p1.met2()
p1.comer("banana")
p1.falar("a")

p1.parar_comer()
p1.falar("a")
p1.comer('sa ad')
p1.parar_falar()
p1.falar('das')

print(p1.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())