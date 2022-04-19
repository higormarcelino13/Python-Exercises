class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria
        
    def get_nome(self):
        return self.__nome
    
    def get_categoria(self):
        return self.__categoria
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_categoria(self, categoria):
        self.__categoria = categoria
        
    def exibir_dados(self):
        print('---------------------')
        print('Nome:', self.get_nome())
        print('Categoria:', self.get_categoria())

class Personagem:
    def __init__(self, nome, nome_vida_real, poderes):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self._poderes = []
        
        for poderes in poderes:
            self.__poderes.append(poderes)
        
    def set_adicionar_super_poder(self):
        if self.get_poder_total() < 3:
            self.__poderes.append(SuperPoder(input('Digite o nome do poder: '), input('Digite a categoria do poder: ')))
        
        
    
class SuperHeroi(Personagem):
    def get_poder_total(self):
        return len(self.__poderes)
    
        
class Vilao(Personagem):
    def tempo_de_prisao(self):
        return self.__tempo_de_prisao
    
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real, poderes)
        self.__tempo_de_prisao = tempo_de_prisao
        
    def __tempo_de_prisao_extra(self):
        return self.__tempo_de_prisao * 0.10
         
        
class Confronto:
    def __init__ (self, superheroi, vilao, poderes):
        self.superheroi = superheroi
        self.vilao = vilao
        
    def get_superheroi(self):
        return self.superheroi
    
    def get_vilao(self):
        return self.vilao
    
    def get_poder_total_superheroi(self):
        return self.superheroi.get_poder_total()
