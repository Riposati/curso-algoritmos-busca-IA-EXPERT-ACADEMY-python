from Mapa import Mapa
    
class Grafo:
    def __init__(self):
        self.mapa = Mapa()
        self.l = []
        
    def dfsAll(self,vertice):
        
        print(f"Cidade visitada - {vertice.nome}")
        #print(f"Situacao do vértice - {vertice.visitado}")
        vertice.visitado = True
        self.l.append(vertice)

        for j in range(len(vertice.adjacentes)):
        
            if vertice.adjacentes[j].cidade.visitado == False:
                print(f"***************** proxima cidade -> {vertice.adjacentes[j].cidade.nome}")
                print("\n")
                #print(f"situacao do vertice -> {vertice.adjacentes[j].cidade.visitado}")
                self.dfsAll(vertice.adjacentes[j].cidade)
                
    def dfs(self,vertice,verticeBuscado):
        
        if vertice.nome == verticeBuscado.nome:
            return True
        
        print(f"Cidade visitada - {vertice.nome}")
        vertice.visitado = True
        self.l.append(vertice)

        for j in range(len(vertice.adjacentes)):
        
            if vertice.adjacentes[j].cidade.visitado == False:
                print(f"***************** proxima cidade -> {vertice.adjacentes[j].cidade.nome}")
                print("\n")
                found = self.dfs(vertice.adjacentes[j].cidade,verticeBuscado)
                if found:
                    return True
                
    def bfsAll(self,vertice):
        
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
            
    def bfs(self,vertice,verticeBuscado):
        
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
'''g.dfs(g.mapa.portoUniao,g.mapa.curitiba)
g.initGrafo()

#print( g.mapa.curitiba.visitado)

print("--------------------------------\n\n")

g.dfsAll(g.mapa.portoUniao)
g.initGrafo()

print("--------------------------------\n\n")

'''

g.bfs(g.mapa.portoUniao, g.mapa.irati)
g.initGrafo()

'''
print("--------------------------------\n\n")
g.BFS(g.mapa.curitiba,g.mapa.contenda)
'''