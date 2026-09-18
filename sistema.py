class Pessoa:
    def __init__(self, nome, telefone):
        self.__nome = nome          
        self.__telefone = telefone  

    
    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone


class Cliente(Pessoa):
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone)
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco

    def mostrar_dados(self):
        print("Nome:", self.get_nome())
        print("Telefone:", self.get_telefone())
        print("Endereço:", self.get_endereco())

class Entregador(Pessoa):
    def __init__(self, nome, telefone, veiculo):
        super().__init__(nome, telefone)
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
        print("\n===== DADOS DA ENTREGA =====")
        print("Cliente:", self.__cliente.get_nome())
        print("Endereço:", self.__cliente.get_endereco())
        print("Entregador:", self.__entregador.get_nome())
        print("Veículo:", self.__entregador.get_veiculo())
        print("Distância:", self.__distancia, "km")
        print("Valor do frete: R$", self.calcular_frete())


class EntregaNormal(Entrega):
    def calcular_frete(self):
        return self._Entrega__distancia * 2


class EntregaExpressa(Entrega):

    def calcular_frete(self):
        return self._Entrega__distancia * 4 + 10 

    def sistema_entrega():

      print("================================") 
      print("       SISTEMA DE ENTREGA       ")
      print("================================")


    nome_cliente = input("Digite o nome do cliente: ")
    telefone_cliente = input("Digite o telefone: ")
    endereco = input("Digite o endereço: ")

    cliente = Cliente(nome_cliente, telefone_cliente, endereco)

    nome_entregador = input("\nDigite o nome do entregador: ")
    telefone_entregador = input("Digite o telefone do entregador: ")
    veiculo = input("Digite o veículo do entregador: ")

    entregador = Entregador(
        nome_entregador,
        telefone_entregador,
        veiculo
    )

    
    distancia = float(input("\nDigite a distância da entrega em km: "))

    print("\nEscolha o tipo de entrega:")
    print("1 - Normal")
    print("2 - Expressa")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        entrega = EntregaNormal(
            cliente,
            entregador,
            distancia
        )

    elif opcao == "2":
        entrega = EntregaExpressa(
            cliente,
            entregador,
            distancia

        )

    else:
        print("Opção inválida!")
        return

    entrega.mostrar_entrega()
    sistema_entrega() gf