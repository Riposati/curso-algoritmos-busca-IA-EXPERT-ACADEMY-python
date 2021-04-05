class Adjacente:
    def __init__(self,cidade, distancia):
        self.cidade = cidade
        self.distancia = distancia # distancia real ( pela estrada )
        self.distanciaAEstrela = self.cidade.distanciaObjetivo + self.distancia