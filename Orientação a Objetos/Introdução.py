# OBJETOS
# Todo tipo de dado em python é um objeto, que possui suas próprias características e métodos.
texto = str('Hello, world!')  # Texto é um objeto da classe Str
lista = list([12, 14, 64, 304])  # lista é um objeto da classe list

# MÉTODOS
# Métodos são ações ou funções estabelecidas dentro de uma determinada classe que interagem com seus objetos.
texto.endswith('world!')  # Chama o método endswith
lista.reverse()  # Chama o método reverse para trocar a ordem da lista
print(lista)


# Os métodos basicamente são funções dispostas dentro das classes e podem ser chamadas com: objeto.função()

# ATRIBUTOS
# Os atributos são as características que todos os objetos instanciados terão.
class Pessoas:
    def __init__(self, nome, idade, gênero):
        self.nome = nome
        self.idade = idade
        self.gênero = gênero


p1 = Pessoas('Leonardo', 18, 'masculino')
print(f'{p1.nome}, {p1.idade}, {p1.gênero}')
# Aqui temos uma classe chamada Pessoas, e os atributos de cada objeto instanciado dessa classe são: nome, idade e gênero.
# Observação: Todo objeto INSTANCIADO é um objeto criado a partir de determinada classe.
