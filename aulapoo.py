print("Olá,todo mundoooo, esse é o meu primeiro código no github!!!!!!!!") 
class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo 
    @property
    def modelo(self):
        return self.__modelo

    def buzinar(self):
        print(f"O carro {self.__modelo} faz: vrum-vrum!")


class Moto:
    def __init__(self, modelo):
        self.__modelo = modelo  
    @property
    def modelo(self):
        return self.__modelo

    def buzinar(self):
        print(f"A moto {self.__modelo} faz: rãdandandan!")



class Aluna:
    def __init__(self, nome):
        self.__nome = nome  

    @property
    def nome(self):
        return self.__nome.upper() 

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou uma aluna!")


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


carro = Carro("civic g10")
carro.buzinar()  

moto = Moto("Honda") 
moto.buzinar()

aluna = Aluna("Maria Eduarda")
aluna.apresentar()  

professor = Professor("Jader", "Matemática")
professor.apresentar() 

