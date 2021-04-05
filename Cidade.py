class Cidade:
    def __init__(self, nome,distanciaObjetivo):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        self.distanciaObjetivo = distanciaObjetivo # heurística usando distancia em linha reta entre as duas cidades
        
    def addCidadeAdjacente(self,cidade):
        self.adjacentes.append(cidade)


