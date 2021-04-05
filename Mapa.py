from Cidade import Cidade
from Adjacente import Adjacente

class Mapa:
    #criação de vértices
    portoUniao = Cidade('Porto União',203)
    pauloFrontin = Cidade('Paulo Frontin',172)
    canoinhas = Cidade('Canoinhas',141)
    irati = Cidade('Irati',139)
    palmeira = Cidade('Palmeira',59)
    campoLargo = Cidade('Campo Largo',27)
    curitiba = Cidade('Curitiba',0)
    balsaNova = Cidade('Balsa Nova',41)
    araucaria = Cidade('Araucária',23)
    saoJosePinhais = Cidade('São José dos Pinhais',13)
    contenda = Cidade('Contenda',39)
    mafra = Cidade('Mafra',94)
    tijucasSul = Cidade('Tijucas do Sul',56)
    lapa = Cidade('Lapa',74)
    saoMateusSul = Cidade('São Mateus do Sul',123)
    tresBarras = Cidade('Três Barras',131)
    
    #criação arestas
    portoUniao.addCidadeAdjacente(Adjacente(pauloFrontin))
    portoUniao.addCidadeAdjacente(Adjacente(canoinhas))
    portoUniao.addCidadeAdjacente(Adjacente(saoMateusSul))
    
    pauloFrontin.addCidadeAdjacente(Adjacente(portoUniao))
    pauloFrontin.addCidadeAdjacente(Adjacente(irati))
    
    canoinhas.addCidadeAdjacente(Adjacente(portoUniao))
    canoinhas.addCidadeAdjacente(Adjacente(tresBarras))
    canoinhas.addCidadeAdjacente(Adjacente(mafra))
    
    irati.addCidadeAdjacente(Adjacente(pauloFrontin))
    irati.addCidadeAdjacente(Adjacente(palmeira))
    irati.addCidadeAdjacente(Adjacente(saoMateusSul))
    
    palmeira.addCidadeAdjacente(Adjacente(irati))
    palmeira.addCidadeAdjacente(Adjacente(campoLargo))
    palmeira.addCidadeAdjacente(Adjacente(saoMateusSul))
    
    campoLargo.addCidadeAdjacente(Adjacente(palmeira))
    campoLargo.addCidadeAdjacente(Adjacente(balsaNova))
    campoLargo.addCidadeAdjacente(Adjacente(curitiba))
    
    curitiba.addCidadeAdjacente(Adjacente(campoLargo))
    curitiba.addCidadeAdjacente(Adjacente(balsaNova))
    curitiba.addCidadeAdjacente(Adjacente(araucaria))
    curitiba.addCidadeAdjacente(Adjacente(saoJosePinhais))
    
    balsaNova.addCidadeAdjacente(Adjacente(curitiba))
    balsaNova.addCidadeAdjacente(Adjacente(campoLargo))
    balsaNova.addCidadeAdjacente(Adjacente(contenda))
    
    araucaria.addCidadeAdjacente(Adjacente(curitiba))
    araucaria.addCidadeAdjacente(Adjacente(contenda))
    
    saoJosePinhais.addCidadeAdjacente(Adjacente(curitiba))
    saoJosePinhais.addCidadeAdjacente(Adjacente(tijucasSul))
    
    contenda.addCidadeAdjacente(Adjacente(balsaNova))
    contenda.addCidadeAdjacente(Adjacente(araucaria))
    contenda.addCidadeAdjacente(Adjacente(lapa))
    
    mafra.addCidadeAdjacente(Adjacente(tijucasSul))
    mafra.addCidadeAdjacente(Adjacente(lapa))
    mafra.addCidadeAdjacente(Adjacente(canoinhas))
    
    tijucasSul.addCidadeAdjacente(Adjacente(mafra))
    tijucasSul.addCidadeAdjacente(Adjacente(saoJosePinhais))
    
    lapa.addCidadeAdjacente(Adjacente(contenda))
    lapa.addCidadeAdjacente(Adjacente(saoMateusSul))
    lapa.addCidadeAdjacente(Adjacente(mafra))
    
    saoMateusSul.addCidadeAdjacente(Adjacente(palmeira))
    saoMateusSul.addCidadeAdjacente(Adjacente(irati))
    saoMateusSul.addCidadeAdjacente(Adjacente(lapa))
    saoMateusSul.addCidadeAdjacente(Adjacente(tresBarras))
    saoMateusSul.addCidadeAdjacente(Adjacente(portoUniao))
    
    tresBarras.addCidadeAdjacente(Adjacente(saoMateusSul))
    tresBarras.addCidadeAdjacente(Adjacente(canoinhas))
    
    
#mapa = Mapa()   
#print(mapa.araucaria.adjacentes)
#for i in range(len(mapa.araucaria.adjacentes)):
#    print(mapa.araucaria.adjacentes[i].cidade.nome)
    
    
    
    
    
    
    
    
    