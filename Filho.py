class Filho:
    def __init__(self, ordemCidade, dados):
        self.ordemCidade = ordemCidade
        self.distTotal = dados.calcDistTotal(ordemCidade)
        #self.distTotal = cC.Cidades().calcDistTotal(self.vetor)