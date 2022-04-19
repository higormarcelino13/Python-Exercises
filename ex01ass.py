class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None #Não tem valor, porque a Pessoa começa sem carro. 
        
    def comprar_carro(self, carro): #Método que recebe um carro.
        self.carro = carro #Adiciona o carro na lista de carros.
        
class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        
    def exibir_dados(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Placa: ", self.placa)
        print("Ano: ", self.ano)
                           
        
meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)                            # imprime: João
print('Modelo do meu carro: ', eu.carro.modelo)         # imprime :Gol
print('Placa do meu carro: ', eu.carro.placa)           # imprime: AAA-1111

