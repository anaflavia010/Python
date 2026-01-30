# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributo de Instância
        self.nome = ''
        self.idade = 0

    # Método de Instância
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f'{self.nome} é Garfonhoto(a) e tem {self.idade} anos de idade.'


# Declaração de Objeto
g1 = Gafanhoto()
g1.nome = 'Ana'
g1.idade = 19
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Eduardo'
g2.idade = 19
g2.aniversario()
print(g2.mensagem())
