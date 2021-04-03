#o grafo em si

from Mapa import Mapa
    
class Grafo:
    def __init__(self):
        self.mapa = Mapa()
        self.l = []
        
    def DFS_all(self,vertice):
        
        print(f"Cidade visitada - {vertice.nome}")
        #print(f"Situacao do vértice - {vertice.visitado}")
        vertice.visitado = True
        self.l.append(vertice)

        for j in range(len(vertice.adjacentes)):
        
            if vertice.adjacentes[j].cidade.visitado == False:
                print(f"***************** proxima cidade -> {vertice.adjacentes[j].cidade.nome}")
                print("\n")
                #print(f"situacao do vertice -> {vertice.adjacentes[j].cidade.visitado}")
                self.DFS_all(vertice.adjacentes[j].cidade)
                
    def DFS(self,vertice,verticeBuscado):
        
        if vertice.nome == verticeBuscado.nome:
            return True
        
        print(f"Cidade visitada - {vertice.nome}")
        vertice.visitado = True
        self.l.append(vertice)

        for j in range(len(vertice.adjacentes)):
        
            if vertice.adjacentes[j].cidade.visitado == False:
                print(f"***************** proxima cidade -> {vertice.adjacentes[j].cidade.nome}")
                print("\n")
                found = self.DFS(vertice.adjacentes[j].cidade,verticeBuscado)
                if found:
                    return True
                
    def BFS_all(self,vertice):
        
        fila = []
        vertice.visitado = True
        self.l.append(vertice)
        fila.append(vertice)
        
        while(fila):
            
            frenteFila = fila.pop(0)
            print(f" FRENTE FILA -> {frenteFila.nome}\n")
            
            for i in range(len(frenteFila.adjacentes)):                
                if frenteFila.adjacentes[i].cidade.visitado == False:                  
                    fila.append(frenteFila.adjacentes[i].cidade)
                    frenteFila.adjacentes[i].cidade.visitado = True
                    self.l.append(frenteFila.adjacentes[i].cidade)
                    print(f"**************vertice enfilerado -> {frenteFila.adjacentes[i].cidade.nome}")
            
    def BFS(self,vertice,verticeBuscado):
        
        fila = []
        vertice.visitado = True
        self.l.append(vertice)
        fila.append(vertice)
        f = False
        
        while(fila and not f):
            
            frenteFila = fila.pop(0)
            print(f" FRENTE FILA -> {frenteFila.nome}\n")
            
            if frenteFila.nome == verticeBuscado.nome:
                print("Achei!\n")
                f = True
            
            for i in range(len(frenteFila.adjacentes)):                
                if frenteFila.adjacentes[i].cidade.visitado == False:                  
                    fila.append(frenteFila.adjacentes[i].cidade)
                    frenteFila.adjacentes[i].cidade.visitado = True
                    self.l.append(frenteFila.adjacentes[i].cidade)
                    print(f"**************vertice enfilerado -> {frenteFila.adjacentes[i].cidade.nome}")
            
    
    def initGrafo(self):
        for i in range(len(self.l)):
            self.l[i].visitado = False
        
    
g = Grafo()
g.DFS(g.mapa.portoUniao,g.mapa.curitiba)
g.initGrafo()

'''#print( g.mapa.curitiba.visitado)

print("--------------------------------\n\n")

g.DFS(g.mapa.curitiba, g.mapa.portoUniao)
g.initGrafo()

print("--------------------------------\n\n")

g.DFS(g.mapa.portoUniao, g.mapa.canoinhas)
g.initGrafo()

print("--------------------------------\n\n")

g.DFS(g.mapa.curitiba, g.mapa.portoUniao)
g.initGrafo()

print("--------------------------------\n\n")

g.DFS_all(g.mapa.portoUniao)
g.initGrafo()

print("--------------------------------\n\n")

g.DFS_all(g.mapa.portoUniao)
g.initGrafo()

g = Grafo()
g.BFS(g.mapa.curitiba,g.mapa.contenda)
g.initGrafo()
print("--------------------------------\n\n")

g.BFS_all(g.mapa.curitiba)
g.initGrafo()

print("--------------------------------\n\n")
g.BFS(g.mapa.curitiba,g.mapa.contenda)
'''