from datetime import datetime
class Pessoa:
    # def falar(self, name): # o self referencia a instancia criada!
    #     print("Estou falando,", name)


    ano_atual = int(datetime.strftime(datetime.now(),'%Y')) # '%Y' retorna ano, '%A' retorna o dia da semana
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
# valor do atributo do obj # valor do parametro

        # var = 'a'
        # print(var)

    # def met2(self):
    #     # print(var) # var nao esta neste escopo
    #     print(self.nome)  # esta com escopo global na classe

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return
        
        if self.falando:
            print(f"{self.nome} nao pode comer enquanto fal a")
            return
        self.comendo = True
        print(f"{self.nome} está comendo {alimento }")
        
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} nao esta comendo")
            return
        print(f"{self.nome} parou de comer")
        
        self.comendo = False
        
    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} nao  pode falar enquanto come")
            return
        if self.falando:
            print(f"{self.nome} ja esta falando")
            return
        print(f"{self.nome} esta falando sobre {assunto}")
        self.falando =  True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} nao esta falando")
            return
        print(f"{self.nome} arou d e falar")


    def get_ano_nascimento(self):
        return self.ano_atual - self.idade