class Pilha:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1
    
    def empilhar(self,cidade):
        if not Pilha.pilhaCheia(self):
            self.top += 1
            self.cidades[self.topo] = cidade
        else:
            print("a pilha ja está cheia")
            
    def desempilhar(self):
        if not Pilha.pilhaVazia(self):
            temp = self.cidades[self.topo]
            self.topo -= 1
            return temp
        else:
            print("A pilha já está vazia")
            return None # null do Python
    
    def getTopo(self):
        return self.cidades[self.topo]
    
    def pilhaVazia(self):
        return (self.topo == -1)
    
    def pilhaCheia(self):
        return (self.topo == self.tamanho-1)