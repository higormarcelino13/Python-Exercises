                   
class Emprego:
    def __init__(self, cargo, area, salario, dependentes):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.dependentes = dependentes
        
    def calcular_salario(self):
        return self.salario + (self.salario * self.dependentes * 0.02)
    
class Pessoa:
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []
        
    def calcular_salario(self):
        return self.emprego.calcular_salario()
    
    def adicionar_dependente(self, dependente):
        self.dependentes.append(dependente)
        
    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Fone: ", self.fone)
        print("Email: ", self.email)
        print("Emprego: ", self.emprego)
        print("Salario: ", self.calcular_salario())



emprego = Emprego("Programador", "TI", 1000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", emprego)

# dois dependentes (o dependente também é um objeto Pessoa)
dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

# adiciona dependentes na lista de dependentes da pessoa1
pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print("Salario: ", pessoa1.calcular_salario())                # imprime 1100.0


