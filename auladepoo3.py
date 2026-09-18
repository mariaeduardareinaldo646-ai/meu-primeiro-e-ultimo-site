class Pessoa:
    def __init__(self, nome, telefone): 
        self.__nome = nome 
        self.__telefone = telefone

    def get_nome(self): 
        return self.__nome 

    def get_telefone(self): 
        return self.__telefone 

class Cliente(Pessoa): 
    def __init__(self, nome, telefone, endereço):
            super().__init__(nome, telefone) 
            self.__endereço = endereço 

    def get_endereço(self):
            return self.__endereço 

    def mostrar_dados(self):
            print("Nome:", self.get_nome()) 
            print("Telefone:", self.get_telefone()) 
            print("Endereço:", self.get_endereço()) 

class Endregador(Pessoa): 
    def __init__(self, nome, telefone, veiculo):
         super().__init__(nome,telefone)
         self.__veiculo = veiculo 

    def get_veiculo(self):
         return self.__veiculo 

    def mostrar_dados(self):
        print("Nome:", self.get_nome())
        print("Telefone:", self.get_telefone())
        print("Veículo:", self.get_veiculo()) 

class Entrega: 
     def __init__(self, cliente, entregador, distancia):
             self.__cliente = cliente
             self.__entregador = entregador
             self.__distancia = distancia 

     def calcular_frete(self):
            return self.__distancia * 2 

     def mostrar_entrega(self): 


 