class Funcionario: 
    def __init__(self, nome, salario_base):
        self.nome = nome 
        self.__salario_base = salario_base 

    def calcular_salario_total(self): 
        return self.__salario_base 

