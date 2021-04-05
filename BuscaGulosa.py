from VetorOrdenado import VetorOrdenado

class BuscaGulosa:
    def __init__(self,objetivo):
        self.objetivo = objetivo
        self.achou = False
    
    def buscar(self, atual):
        print("\nAtual: {}".format(atual.nome))
        atual.visitado = True
        
        if atual == self.objetivo:
            self.achou = True
        else:
            self.fronteira = VetorOrdenado(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a.cidade)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                BuscaGulosa.buscar(self, self.fronteira.getPrimeiro())

from Mapa import Mapa
mapa = Mapa()
buscaGulosa = BuscaGulosa(mapa.curitiba)
buscaGulosa.buscar(mapa.portoUniao)