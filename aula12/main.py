class Animal_domestico:
    def __init__(self, nome, raca, peso):
        self.nome = nome
        self.raca = raca
        self.peso = peso

class Cachorro(Animal_domestico):
    def __init__(self, nome, raca, peso):
        super().__init__(nome, raca, peso)

    def comer(self):
        return "croc croc croc"

class Gato(Animal_domestico):
    def __init__(self, nome, raca, peso, instinto):
        super().__init__(nome, raca, peso)
        self.instinto = instinto

    def derrubar(self):
        return f"O {super().nome} derrubou algo"

gato1 = Gato(nome="Alfredo", raca="Persa", peso=2, instinto=8001)
cachorro1 = Cachorro(nome="Seila", raca="Vira lata", peso=3, coisa_nova="Alguma coisa")
    