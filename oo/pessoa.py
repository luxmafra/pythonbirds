class Pessoa:
    def __init__(self, nome = None, idade = 30):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá {}'.format(id(self))

if __name__ == '__main__':
    p = Pessoa('Renzo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Lucas'
    print(p.nome)
    print(p.idade)

