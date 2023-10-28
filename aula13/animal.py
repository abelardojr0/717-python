class Animal:
    def __init__(self, especie, raca, cor, idade):
        self.especie = especie
        self.raca = raca
        self.cor = cor
        self.idade = idade
    
    def comer(self, alimento):
        return f"O {self.especie} comeu o {alimento}"
    
    def som(self):
        return "Som indefinido"

class Cachorro(Animal):
    def __init__(self, raca, cor, idade):
        super().__init__(especie = "cachorro", raca=raca, cor=cor, idade=idade)
    
    def som(self):
        return "Au au"
    
class Gato(Animal):
    def __init__(self, raca, cor, idade):
        super().__init__(especie = "gato", raca=raca, cor=cor, idade=idade)

    def som(self):
        return "Miau"
    
cachorro1 = Cachorro(raca="Pinsher", cor="caramelo", idade=1)
gato1 = Gato(raca="Siamês", cor="branco", idade=3)

print(cachorro1.som())
print(gato1.som())

