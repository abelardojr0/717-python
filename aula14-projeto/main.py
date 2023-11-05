class Jogador:
    def __init__(self, nome:str, time:str, numero:int):
        self.__nome = nome
        self.__time = time
        self.__numero = numero
    


    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_nome):
        self.__nome = novo_nome
        return self.nome



    def getTime(self):
        return self.__time
    
    def setTime(self, novo_time):
        self.__time = novo_time
        return self.time




    def getNumero(self):
        return self.__numero
    
    def setNumero(self, novo_numero):
        self.__numero = novo_numero
        return self.numero
    




class Comissao:
    def __init__(self, nome:str, time:str, formacao:str):
        self.__nome = nome
        self.__time = time
        self.__formacao = formacao

    def dar_coletiva(self):
        return "Algum membro da comissão está dando coletiva"
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_nome):
        self.__nome = novo_nome
        return self.nome
    

    def getTime(self):
        return self.__time
    
    def setTime(self, novo_time):
        self.__time = novo_time
        return self.time
    

    def getFormacao(self):
        return self.__formacao
    
    def setFormacao(self, novo_formacao):
        self.__formacao = novo_formacao
        return self.formacao
        


class Tecnico(Comissao):
    def __init__(self, nome: str, time: str, formacao: str):
        super().__init__(nome, time, formacao)
    
    def dar_coletiva(self):
        return f"O técnico {self.getNome()} está dando coletiva"
    

class Auxiliar(Comissao):
    def __init__(self, nome: str, time: str, formacao: str):
        super().__init__(nome, time, formacao)
    
    def dar_coletiva(self):
        return f"O auxiliar {self.getNome()} está dando coletiva"
    

class Preparador(Comissao):
    def __init__(self, nome: str, time: str, parte_elenco: str):
        super().__init__(nome, time, parte_elenco)
        self.__parte_elenco = parte_elenco
    
    def getParteElenco(self):
        return self.__parte_elenco

    def setParteElenco(self, nova_parte_elenco):
        self.__parte_elenco = nova_parte_elenco
        return self.__parte_elenco

    def dar_coletiva(self):
        return f"O Preparador {self.getNome()} está dando coletiva"

while True:
    menu = int(input("""
        1 - Cadastrar Jogador
        2 - Cadastrar Time
        3 - Cadastrar Comissão Técnica
        4 - O técnico dar coletiva
        5 - O auxiliar dar coletiva
        6 - O preparador dar coletiva
        0 - Sair
    """))

    match menu:
        case 1:
            nome = str(input("Digite o nome do jogador: "))
            time = str(input("Digite o time do jogador:"))
            numero = int(input("Digite o número da camisa do jogador:"))
            jogador = Jogador(nome=nome, time=time, numero=numero)
        case 2:
            print("Cadastar Time")
        case 3:
            nome_tecnico = str(input("Digite o nome do tecnico: "))
            time_tecnico = str(input("Digite o time do tecnico: "))
            formacao_tecnico = str(input("Digite o formação do tecnico: "))
            tecnico = Tecnico(nome=nome_tecnico, time=time_tecnico, formacao= formacao_tecnico)


            nome_auxiliar = str(input("Digite o nome do auxiliar: "))
            time_auxiliar = str(input("Digite o time do auxiliar: "))
            formacao_auxiliar = str(input("Digite o formação do auxiliar: "))
            auxiliar = Auxiliar(nome=nome_auxiliar, time=time_auxiliar, formacao= formacao_auxiliar)


            nome_preparador = str(input("Digite o nome do preparador: "))
            time_preparador = str(input("Digite o time do preparador: "))
            parte_elenco_preparador = str(input("Digite a parte do elenco do preparador: "))
            preparador = Preparador(nome=nome_preparador, time=time_preparador, parte_elenco= parte_elenco_preparador)


        case 4:
            print(tecnico.dar_coletiva())
        case 5:
            print(auxiliar.dar_coletiva())
        case 6:
            print(preparador.dar_coletiva())

        case 0:
            print("Obrigado por usar o programa, tchau!")
            break
        case _:
            print("Opção Inválida")


