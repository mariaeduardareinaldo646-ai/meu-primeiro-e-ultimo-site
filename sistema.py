
class Loja:

  def __init__(self, nome_loja, endereco):
    self.nome_loja = nome_loja
    self.endereco = endereco

  def mostrar_loja(self):
    print(f"Loja: {self.nome_loja} - Endereço: {self.endereco}")



class Produto1:

  def __init__(self, nome, preco, estoque):
    self.nome = nome
    self.__preco = preco 
    self.estoque = estoque

  
  @property
  def preco(self):
    return self.__preco

  def mostrar_produtos(self):
    print(f"Produto: {self.nome} - R$ {self.__preco}")
    print(f"Estoque: {self.estoque}")


class Produto2:

  def __init__(self, nome, preco, estoque):
    self.nome = nome
    self.__preco = preco 
    self.estoque = estoque

  
  @property
  def preco(self):
    return self.__preco

  def mostrar_produtos(self):
    print(f"Produto: {self.nome} - R$ {self.__preco}")
    print(f"Estoque: {self.estoque}")



class Produto3:

  def __init__(self, nome, preco, estoque):
    self.nome = nome
    self.__preco = preco 
    self.estoque = estoque

  
  @property
  def preco(self):
    return self.__preco

  def mostrar_produtos(self):
    print(f"Produto: {self.nome} - R$ {self.__preco}")
    print(f"Estoque: {self.estoque}")


class Produto4:

  def __init__(self, nome, preco, estoque):
    self.nome = nome
    self.__preco = preco 
    self.estoque = estoque

  
  @property
  def preco(self):
    return self.__preco

  def mostrar_produtos(self):
    print(f"Produto: {self.nome} - R$ {self.__preco}")
    print(f"Estoque: {self.estoque}")


class Produto5:

  def __init__(self, nome, preco, estoque):
    self.nome = nome
    self.__preco = preco 
    self.estoque = estoque

  
  @property
  def preco(self):
    return self.__preco

  def mostrar_produtos(self):
    print(f"Produto: {self.nome} - R$ {self.__preco}")
    print(f"Estoque: {self.estoque}")



class Pessoa:

  def __init__(self, nome):
    self.nome = nome



class Cliente1(Pessoa):

  def __init__(self, nome_pessoa, nome_produto):
    super().__init__(nome_pessoa)  
    self.nome_produto = nome_produto

  def mostrar_comp(self):
    print(f"{self.nome} comprou {self.nome_produto}")

class Cliente2(Pessoa):

  def __init__(self, nome_pessoa, nome_produto):
    super().__init__(nome_pessoa)  
    self.nome_produto = nome_produto

  def mostrar_comp(self):
    print(f"{self.nome} comprou {self.nome_produto}")



class Funcionario1(Pessoa):

  def __init__(self, nome_fun, pedido):
    super().__init__(nome_fun)  
    self.pedido = pedido

  def entregar(self):
    print(f"{self.nome} entregou {self.pedido}")
    print("Pedido entregue")

class Funcionario2(Pessoa):

  def __init__(self, nome_fun, pedido):
    super().__init__(nome_fun)  
    self.pedido = pedido

  def entregar(self):
    print(f"{self.nome} entregou {self.pedido}")
    print("Pedido entregue")


produto = Produto1("Kit: shampoo, condicionador, mascara de hidratação", 120, 80) 
produto = Produto2("Creme para cabelos cacheados, e lisos", 50, 80) 
produto = Produto3("Kit: Óleo de tratamendo coco, super óleo e multibenefícios", 60, 70) 
produto = Produto4("Kit: Creme e gelatina", 70, 50) 
produto = Produto5("Kit: Creme e óleo de cabelo", 60, 90) 

cliente = Cliente1("Mikaelle Melo", "shampoo, condicionador, mascara de hidratação")
cliente = Cliente2("Sofia Gomes", "Kit: Óleo de tratamendo coco, super óleo e multibenefícios")

funcionario = Funcionario1("Francisco Raimundo", "shampoo, condicionador, mascara de hidratação") 
funcionario = Funcionario2("Alfredo Texugueiro", "Kit: Óleo de tratamendo coco, super óleo e multibenefícios")

loja = Loja("Loja Principal", "Rua Girassol, 67")



loja.mostrar_loja()
print("-" * 50)
produto.mostrar_produtos3()
print("-" * 50) 
Produto1.mostrar_produtos()
print("-" * 50)
Cliente1.mostrar_comp() 
print("-" * 50) 
Cliente2.mostrar_comp() 
print("-" * 50)
Funcionario1.entregar() 
Funcionario2.entregar()