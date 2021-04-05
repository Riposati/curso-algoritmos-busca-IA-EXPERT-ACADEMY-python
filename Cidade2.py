class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome
        self.visitado = False
        self.distanciaObjetivo = distanciaObjetivo # heurística usando distancia em linha reta entre as duas cidades
        self.adjacentes = []
        
    def addCidadeAdjacente(self,cidade):
        self.adjacentes.append(cidade)



