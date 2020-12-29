# Definindo uma classe mãe:
class Main:
    def __init__(self, altura, idade, peso):
        self.altura = altura
        self.idade = idade
        self.peso = peso

    def teste(self):
        print('A pessoa existe...')


class Herdada(Main):
    def __init__(self, altura, idade, peso, cor_dos_olhos):
        super().__init__(altura, idade, peso)
        self.cor_dos_olhos = cor_dos_olhos


p1 = Main(1.80, 18, 65)
p1.teste()
p2 = Herdada(1.70, 17, 54, 'azuis')
p2.teste()