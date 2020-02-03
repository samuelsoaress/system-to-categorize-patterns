class InfoDataset():
    def __init__(self, total, resto, categorizado):
        self.total = total
        self.resto = resto
        self.categorizado = categorizado



class Palavra():
    def __init__(self,nome,categoria, id=None):
        self.nome = nome
        self.categoria = categoria
