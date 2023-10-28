import datetime

class Funcionario:
    def __init__(self, nome, cpf, data_nasc, cep):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.cep = cep
        
    def bater_ponto(self):
        agora = datetime.datetime.now()
        hora_atual = agora.hour
        minutor_atual = agora.minute

        return f"O {self.nome} bateu o ponto as {hora_atual}:{minutor_atual}"

class Gerente(Funcionario):
    def __init__(self, nome, cpf, data_nasc, cep, login, senha):
        super().__init__(nome, cpf, data_nasc, cep)
        self.login = login
        self.senha = senha
    
    def contratar(self):
        return f"O gerente {self.nome} contratou fulano"

    def demitir(self):
        return f"O gerente {self.nome} demitiu fulano"
    
    def bater_ponto(self):
        agora = datetime.datetime.now()
        hora_atual = agora.hour
        minutor_atual = agora.minute

        return f"O {self.nome} bateu o ponto as outra parada diferente {hora_atual}:{minutor_atual}"

class Coordenador(Funcionario):
    def __init__(self, nome, cpf, data_nasc, cep):
        super().__init__(nome, cpf, data_nasc, cep)
    
    def gerar_relatorio(self):
        return f"Relatório gerado pelo coordenador {self.nome}"
    

funcionario_comum = Funcionario(nome="João", cpf="000", data_nasc="10",cep="1")
gerente1 = Gerente(nome="Maria", cpf="111", data_nasc="20",cep="2", login="maria", senha="123")
coordenador1 = Coordenador(nome="Abel", cpf="222", data_nasc="30",cep="3")


print(coordenador1.bater_ponto())