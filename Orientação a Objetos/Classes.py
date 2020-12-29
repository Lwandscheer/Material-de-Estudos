# CLASSE
# Uma determinada classe é um molde que agrupará atributos e métodos de seus objetos pertencentes.
class Calc:
    def __init__(self, valorA, valorB):
        self.valorA = valorA
        self.valorB = valorB

    # Métodos da classe Calc:
    # Método de soma
    def somar(self):
        soma = self.valorA + self.valorB  # Para retornar um atributo, use o self.atributo
        print(soma)

    # Método de subtração
    def subtrair(self):
        loop = True
        while loop:
            chave = input('>> Escolha o conjunto da subtração: ')
            if chave == 'ab':
                print(self.valorA - self.valorB)
                loop = False
            elif chave == 'ba':
                print(self.valorB - self.valorA)
                loop = False
            elif chave == 'bb':
                print(self.valorB - self.valorB)
                loop = False
            elif chave == 'aa':
                print(self.valorA - self.valorA)
                loop = False
            else:
                print('Valor incorreto. Tente novamente...')

    # Método de multiplicação
    def multiplicação(self):
        print(self.valorA * self.valorB)

    # Método de divisão
    def divisão(self):
        loop = True
        while loop:
            chave = input('>> Escolha o conjunto da divisão: ')
            if chave == 'ab':
                print(self.valorA / self.valorB)
                loop = False
            elif chave == 'ba':
                print(self.valorB / self.valorA)
                loop = False
            else:
                print('Impossivel dividir por zero...')


# instanciando objeto e interagindo com métodos:
# Evitar utilizar 0 devido ao método divisão.
ex1 = Calc(5, 10)
ex1.somar()
ex1.subtrair()
ex1.divisão()
