class Veiculo:
    def __init__(self, nome:str, motores:int, rodas:bool):
        self.nome = nome
        self.motores = motores
        self.rodas = rodas
    
    def informacoes(self):
        return f"""
            Nome: {self.nome}
            Quantidade de motores: {self.motores}
            Possuir rodas: {self.rodas}
        """

    def buzinar(self):
        return "Som indefinido"
    
class Carro(Veiculo):
    def __init__(self, nome: str, motores: int, rodas: bool):
        super().__init__(nome, motores, rodas)
    
    def buzinar(self):
        return "Biiiiii"

class Navio(Veiculo):
    def __init__(self, nome: str, motores: int, rodas: bool):
        super().__init__(nome, motores, rodas)

    def buzinar(self):
        return "Fommmmmmm"

class Aviao(Veiculo):
    def __init__(self, nome: str, motores: int, rodas: bool):
        super().__init__(nome, motores, rodas)
    
    def buzinar(self):
        return "Será que avião tem buzina?"
    


aviao1 = Aviao(nome="Boing", motores=4, rodas=True)
carro1 = Carro(nome="Esportivo", motores=1, rodas=True)
navio1 = Navio(nome="Titanic", motores=16, rodas=False)

print(aviao1.buzinar())
print(carro1.buzinar())
print(navio1.buzinar())

print(carro1.informacoes())