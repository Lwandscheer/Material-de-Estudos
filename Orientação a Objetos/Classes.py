# CLASSE
# Uma determinada classe é um molde que agrupará atributos e métodos de seus objetos pertencentes.
class Calc:
    def __init__(self, valorA, valorB):
        self.valorA = valorA
        self.valorB = valorB

    def somar(self):
        soma = self.valorA + self.valorB
        print(soma)

    def subtrair(self):
        loop = True
        while loop:
            chave = input('>> Escolha o conjunto da subtração: ')
            if chave == 'AB':
                print(self.valorA - self.valorB)
                loop = False
            elif chave == 'BA':
                print(self.valorB - self.valorA)
                loop = False
            elif chave == 'BB':
                print(self.valorB - self.valorB)
                loop = False
            elif chave == 'AA':
                print(self.valorA - self.valorA)
                loop = False
            else:
                print('Valor incorreto. Tente novamente...')


ex1 = Calc(5, 10)
ex1.somar()
ex1.subtrair()