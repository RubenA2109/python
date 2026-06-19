class Pessoa:
    total_pessoas = 0
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1
        
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"
    
    # Getter para o nome da pessoa
    @property
    def nome(self):
        return self.__nome
    
    # Setter para idade
    @nome.setter
    def nome(self,novo_nome):
        if len(novo_nome) < 2:
            print("Nome inválido")
        else: self.__nome = novo_nome
        
    # Getter para a idade da pessoa
    @property
    def idade(self):
        return self.__idade
    
    # Setter para idade
    @idade.setter
    def idade(self,nova_idade):
        if len(nova_idade) < 0:
            print("idade inválida")
        else: self.__nome = nova_idade
        
    def aumentarIdade(self):
        return self.idade +10
    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, area_trabalho, anos_trabalho):
        super().__init__(nome, idade)
        self.area_trabalho = area_trabalho
        self.anos_trabalho = anos_trabalho
    
# AREA DE TESTE
p1 = Pessoa("Marcelo", 52)
p2 = Pessoa("Sergio", 19)
p3 = Pessoa("Tomas", 18)
f1 = Funcionario("Ana",23,"Textil",3)
print(f1.aumentarIdade())
print(p1.nome)
print(Pessoa.total_pessoas)
print(p2)