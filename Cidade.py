class Cidade:
    def __init__(self, nome,distanciaObjetivo):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        self.distanciaObjetivo = distanciaObjetivo # heurística usando distancia euclidiana entre a cidade atual e a cidade objetivo
        
    def addCidadeAdjacente(self,cidade):
        self.adjacentes.append(cidade)


