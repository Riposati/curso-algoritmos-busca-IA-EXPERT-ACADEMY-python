from Fila import Fila

class Largura:
    def __init__(self,inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(20)
        self.fronteira.enfileirar(inicio)
        self.achouObjetivo = False
        
    def buscarAll(self):
        primeiro = self.fronteira.getPrimeiro()
        print("Primeiro: {}".format(primeiro.nome))
        
        temp = self.fronteira.desenfileirar()
        print("Desenfileirou: {}".format(temp.nome))
        
        for a in primeiro.adjacentes:
            print("Verificado se já visitado: {}".format(a.cidade.nome))
            if a.cidade.visitado == False:
                a.cidade.visitado = True
                self.fronteira.enfileirar(a.cidade)
        if self.fronteira.numeroElementos > 0:
            Largura.buscarAll(self)
            
    def buscarObjetivo(self):
        primeiro = self.fronteira.getPrimeiro()
        print("Primeiro: {}".format(primeiro.nome))
        
        if primeiro == self.objetivo:
            self.achouObjetivo = True
        else:
            temp = self.fronteira.desenfileirar()
            print("Desenfileirou: {}".format(temp.nome))
            
            for a in primeiro.adjacentes:
                print("Verificado se já visitado: {}".format(a.cidade.nome))
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.enfileirar(a.cidade)
            if self.fronteira.numeroElementos > 0:
                Largura.buscarObjetivo(self)

from Mapa import Mapa
mapa = Mapa()
largura = Largura(mapa.portoUniao, mapa.irati)
largura.buscarAll()
        