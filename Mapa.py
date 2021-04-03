from Cidade import Cidade
from Adjacente import Adjacente

class Mapa:
    #criação de vértices
    portoUniao = Cidade('Porto União')
    pauloFrontin = Cidade('Paulo Frontin')
    canoinhas = Cidade('Canoinhas')
    irati = Cidade('Irati')
    palmeira = Cidade('Palmeira')
    campoLargo = Cidade('Campo Largo')
    curitiba = Cidade('Curitiba')
    balsaNova = Cidade('Balsa Nova')
    araucaria = Cidade('Araucária')
    saoJosePinhais = Cidade('São José dos Pinhais')
    contenda = Cidade('Contenda')
    mafra = Cidade('Mafra')
    tijucasSul = Cidade('Tijucas do Sul')
    lapa = Cidade('Lapa')
    saoMateusSul = Cidade('São Mateus do Sul')
    tresBarras = Cidade('Três Barras')
    
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
    
    
    
    
    
    
    
    
    