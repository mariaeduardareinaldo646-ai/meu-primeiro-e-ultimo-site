class Loja:

    def __init__(self, nome_loja, endereco):
        self.nome_loja = nome_loja
        self.endereco = endereco

    def mostrar_loja(self):
        print("Loja:", self.nome_loja)
        print("Endereço:", self.endereco)



class Produto:

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.__preco = preco
        self.estoque = estoque

    def get_preco(self):
        return self.__preco

    def mostrar_produto(self):
        print("Produto:", self.nome)
        print("Preço: R$", self.__preco)
        print("Estoque:", self.estoque)


class Pessoa:

    def __init__(self, nome):
        self.nome = nome


class Cliente(Pessoa):

    def __init__(self, nome, produto):
        super().__init__(nome)
        self.produto = produto

    def mostrar_compra(self):
        print(self.nome, "comprou", self.produto)


class Funcionario(Pessoa):

    def __init__(self, nome, pedido):
        super().__init__(nome)
        self.pedido = pedido

    def entregar(self):
        print(self.nome, "está entregando:", self.pedido)
        print("Pedido entregue!")




loja = Loja(
    "Loja Principal",
    "Rua Girassol, 67"
)



produto1 = Produto(
    "Kit shampoo, condicionador e máscara",
    120,
    80
)

produto2 = Produto(
    "Creme para cabelos cacheados e lisos",
    50,
    80
)

produto3 = Produto(
    "Kit óleo de tratamento de coco",
    60,
    70
)

produto4 = Produto(
    "Kit creme e gelatina",
    70,
    50
)

produto5 = Produto(
    "Kit creme e óleo de cabelo",
    60,
    90
)




loja.mostrar_loja()

print("-" * 50)


produto1.mostrar_produto()

print("-" * 50)

produto2.mostrar_produto()

print("-" * 50)

produto3.mostrar_produto()

print("-" * 50)

produto4.mostrar_produto()

print("-" * 50)

produto5.mostrar_produto()

print("-" * 50)



cliente1 = Cliente(
    "Mikaelle Melo",
    "Kit shampoo, condicionador e máscara"
)

cliente2 = Cliente(
    "Sofia Gomes",
    "Kit óleo de tratamento de coco"
)


cliente1.mostrar_compra()

cliente2.mostrar_compra()

print("-" * 50)




funcionario1 = Funcionario(
    "Francisco Raimundo",
    "Kit shampoo, condicionador e máscara"
)

funcionario2 = Funcionario(
    "Alfredo Texugueiro",
    "Kit óleo de tratamento de coco"
)


funcionario1.entregar()

print("-" * 50)

funcionario2.entregar()
