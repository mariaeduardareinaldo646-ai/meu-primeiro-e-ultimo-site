```python
# ============================================
# SISTEMA DE LOJA
# ============================================


# CLASSE PESSOA
class Pessoa:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    # Funções para acessar os dados privados
    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone


# HERANÇA
# Cliente herda da classe Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone)
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco


# CLASSE PRODUTO
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    # Encapsulamento
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # Função que será sobrescrita
    def calcular_preco(self):
        return self.__preco


# HERANÇA + POLIMORFISMO
class ProdutoPromocao(Produto):
    def __init__(self, nome, preco, desconto):
        super().__init__(nome, preco)
        self.__desconto = desconto

    # Polimorfismo
    def calcular_preco(self):
        desconto = self.get_preco() * self.__desconto / 100
        return self.get_preco() - desconto


# HERANÇA + POLIMORFISMO
class ProdutoImportado(Produto):
    def __init__(self, nome, preco, taxa):
        super().__init__(nome, preco)
        self.__taxa = taxa

    # Polimorfismo
    def calcular_preco(self):
        taxa = self.get_preco() * self.__taxa / 100
        return self.get_preco() + taxa


# CLASSE LOJA
class Loja:
    def __init__(self, nome):
        self.__nome = nome
        self.__produtos = []

    # Encapsulamento
    def get_nome(self):
        return self.__nome

    # Função para adicionar produtos
    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    # Função para mostrar produtos
    def mostrar_produtos(self):
        print("\n================================")
        print("        PRODUTOS DA LOJA")
        print("================================")

        if len(self.__produtos) == 0:
            print("Nenhum produto cadastrado.")
            return

        for i, produto in enumerate(self.__produtos, 1):
            print("\nProduto", i)
            print("Nome:", produto.get_nome())
            print(
                "Preço: R$",
                f"{produto.calcular_preco():.2f}"
            )


# FUNÇÃO PRINCIPAL
def sistema_loja():

    print("================================")
    print("          SISTEMA DE LOJA")
    print("================================")

    nome_loja = input("Digite o nome da loja: ")

    loja = Loja(nome_loja)

    quantidade = int(
        input("\nQuantos produtos deseja cadastrar? ")
    )

    for i in range(quantidade):

        print("\n-------------------------------")
        print("CADASTRO DO PRODUTO", i + 1)
        print("-------------------------------")

        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: R$ "))

        print("\nEscolha o tipo do produto:")
        print("1 - Produto normal")
        print("2 - Produto em promoção")
        print("3 - Produto importado")

        tipo = input("Digite sua opção: ")

        if tipo == "1":

            produto = Produto(nome, preco)

        elif tipo == "2":

            desconto = float(
                input("Digite o desconto (%): ")
            )

            produto = ProdutoPromocao(
                nome,
                preco,
                desconto
            )

        elif tipo == "3":

            taxa = float(
                input("Digite a taxa de importação (%): ")
            )

            produto = ProdutoImportado(
                nome,
                preco,
                taxa
            )

        else:
            print("Opção inválida!")
            continue

        loja.adicionar_produto(produto)

    loja.mostrar_produtos()


sistema_loja()