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
    portoUniao.addCidadeAdjacente(Adjacente(pauloFrontin,46))
    portoUniao.addCidadeAdjacente(Adjacente(canoinhas,78))
    portoUniao.addCidadeAdjacente(Adjacente(saoMateusSul,87))
    
    pauloFrontin.addCidadeAdjacente(Adjacente(portoUniao,46))
    pauloFrontin.addCidadeAdjacente(Adjacente(irati,75))
    
    canoinhas.addCidadeAdjacente(Adjacente(portoUniao,78))
    canoinhas.addCidadeAdjacente(Adjacente(tresBarras,12))
    canoinhas.addCidadeAdjacente(Adjacente(mafra,66))
    
    irati.addCidadeAdjacente(Adjacente(pauloFrontin,75))
    irati.addCidadeAdjacente(Adjacente(palmeira,75))
    irati.addCidadeAdjacente(Adjacente(saoMateusSul,57))
    
    palmeira.addCidadeAdjacente(Adjacente(irati,75))
    palmeira.addCidadeAdjacente(Adjacente(campoLargo,55))
    palmeira.addCidadeAdjacente(Adjacente(saoMateusSul,77))
    
    campoLargo.addCidadeAdjacente(Adjacente(palmeira,55))
    campoLargo.addCidadeAdjacente(Adjacente(balsaNova,22))
    campoLargo.addCidadeAdjacente(Adjacente(curitiba,29))
    
    curitiba.addCidadeAdjacente(Adjacente(campoLargo,29))
    curitiba.addCidadeAdjacente(Adjacente(balsaNova,51))
    curitiba.addCidadeAdjacente(Adjacente(araucaria,37))
    curitiba.addCidadeAdjacente(Adjacente(saoJosePinhais,15))
    
    balsaNova.addCidadeAdjacente(Adjacente(curitiba,51))
    balsaNova.addCidadeAdjacente(Adjacente(campoLargo,22))
    balsaNova.addCidadeAdjacente(Adjacente(contenda,19))
    
    araucaria.addCidadeAdjacente(Adjacente(curitiba,37))
    araucaria.addCidadeAdjacente(Adjacente(contenda,18))
    
    saoJosePinhais.addCidadeAdjacente(Adjacente(curitiba,15))
    saoJosePinhais.addCidadeAdjacente(Adjacente(tijucasSul,49))
    
    contenda.addCidadeAdjacente(Adjacente(balsaNova,19))
    contenda.addCidadeAdjacente(Adjacente(araucaria,18))
    contenda.addCidadeAdjacente(Adjacente(lapa,26))
    
    mafra.addCidadeAdjacente(Adjacente(tijucasSul,99))
    mafra.addCidadeAdjacente(Adjacente(lapa,57))
    mafra.addCidadeAdjacente(Adjacente(canoinhas,66))
    
    tijucasSul.addCidadeAdjacente(Adjacente(mafra,99))
    tijucasSul.addCidadeAdjacente(Adjacente(saoJosePinhais,49))
    
    lapa.addCidadeAdjacente(Adjacente(contenda,26))
    lapa.addCidadeAdjacente(Adjacente(saoMateusSul,60))
    lapa.addCidadeAdjacente(Adjacente(mafra,57))
    
    saoMateusSul.addCidadeAdjacente(Adjacente(palmeira,77))
    saoMateusSul.addCidadeAdjacente(Adjacente(irati,57))
    saoMateusSul.addCidadeAdjacente(Adjacente(lapa,60))
    saoMateusSul.addCidadeAdjacente(Adjacente(tresBarras,43))
    saoMateusSul.addCidadeAdjacente(Adjacente(portoUniao,87))
    
    tresBarras.addCidadeAdjacente(Adjacente(saoMateusSul,43))
    tresBarras.addCidadeAdjacente(Adjacente(canoinhas,12))
    
    
#mapa = Mapa()   
#print(mapa.araucaria.adjacentes)
#for i in range(len(mapa.araucaria.adjacentes)):
#    print(mapa.araucaria.adjacentes[i].cidade.nome)
    
    
    
    
    
    
    
    
    