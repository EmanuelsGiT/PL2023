class Pessoa:
    def __init__(self,idade,sexo,tensao,colesterol,batimento,temDoenca):
        self.idade = idade
        self.sexo = sexo
        self.tensao = tensao
        self.colesterol = colesterol
        self.batimento = batimento
        self.temDoenca = temDoenca

    def __str__(self):
        return f"{self.idade},{self.sexo},{self.tensao},{self.colesterol},{self.batimento},{self.temDoenca}"