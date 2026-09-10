print("ola,mundo") 
class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo 
    @property
    def modelo(self):
        return self.__modelo

    def buzinar(self):
        print(f"O carro {self.__modelo} faz: BIBIBIBIBIBIBIBIBIBI!")


class Moto:
    def __init__(self, modelo):
        self.__modelo = modelo  
    @property
    def modelo(self):
        return self.__modelo

    def buzinar(self):
        print(f"A moto {self.__modelo} faz: VRUUUUUUUUUUUUUUUUUUUUUUUM!")



class Aluno:
    def __init__(self, nome):
        self.__nome = nome  

    @property
    def nome(self):
        return self.__nome.upper() 

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um aluno!")


class Professor:
    def __init__(self, nome, materia):
        self.__nome = nome
        self.__materia = materia  

    @property
    def nome(self):
        return self.__nome

    @property
    def materia(self):
        return self.__materia

    def apresentar(self):
        print(f"Olá, sou o professor {self.__nome} e dou aulas de {self.__materia}!")



class Esporte: 
    def __init__(self, nome_esporte, numero_jogadores):
        self.__nome = nome_esporte
        self.__jogadores = numero_jogadores

    @property
    def jogadores(self):
        return self.__jogadores

    
    @jogadores.setter
    def jogadores(self, quantidade):
        if quantidade > 0:
            self.__jogadores = quantidade
        else:
            print("Erro: Um esporte precisa de pelo menos 1 jogador.")

    def jogar(self):
        print(f"Estou jogando {self.__nome} com {self.__jogadores} jogadores!")



carro = Carro("Fusca")
carro.buzinar()  

moto = Moto("Honda") 
moto.buzinar()

aluno = Aluno("Carlos")
aluno.apresentar()  

professor = Professor("João", "Matemática")
professor.apresentar() 

futebol = Esporte("Futebol", 11)
basquete = Esporte("Basquete", 5) 

futebol.jogar()
basquete.jogar() 
