class Celular: 
    def __init__(self, modelo): 
        self.modelo = modelo 
        self._bateria = 100 

    @property 
    def bateria(self):
        return f"{self._bateria}%" 

    @bateria.setter 
    def bateria(self, nova_carga): 
        if 0 <= nova_carga <= 100: 
            self._bateria = nova_carga 
        else: 
            print("Erro: A carga da bateria deve ser entre 0 e 100!!")  

meu_celular = Celular("Iphone 18 pro max") 
print(meu_celular.bateria)  
meu_celular.bateria = 150 

