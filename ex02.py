class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas   
        
    def exibir_dados(self):
        print('---------------------')
        print('Nome:', self.nome)
        print('Cor:', self.cor)
        print('Numero de Patas:', self.numero_patas)
        
class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas)
        self.raca = raca
        
    def exibir_dados(self):
        super().exibir_dados()
        print('Raca:', self.raca)

        

animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados()       # exibe os atributos do animal

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados()          # exibe os atributos do cachorro
