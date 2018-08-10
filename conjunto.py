import itertools

class Conjunto:
    
    def __init__(self):
        self.conjunto = []
        
    def adicionar(self, item):
        if item not in self.conjunto:
            self.conjunto.append(item)

    def remover(self, item):
        self.conjunto.remove(item)

    def pertinencia(self, item):
        return item in self.conjunto

    def contido(self, conjunto):
        for i in conjunto:
            if i not in self.conjunto:
                return False
        return True

    def uniao(self, conjunto):
        conjuntoResultado = conjunto
        for i in itertools.chain(self.conjunto, conjunto):
            conjuntoResultado.append(i)
        return conjuntoResultado

    def interseccao(self, conjunto):
        conjuntoResultado = []
        for i in self.conjunto:
            if i in conjunto:
                conjuntoResultado.append(i)
        return conjuntoResultado

    def diferenca(self, conjunto):
        conjuntoResultado = []
        for i in self.conjunto:
            if i not in conjunto:
                conjuntoResultado.append(i)
        return conjuntoResultado

    def complemento(self, conjunto):
        conjuntoResultado = []
        for i in self.conjunto:
            if i not in conjunto:
                conjuntoResultado.append(i)
        return conjuntoResultado

    def cartesiano(self, conjunto):
        conjuntoResultado = []
        for elemento in itertools.product(self.conjunto, conjunto):
            conjuntoResultado.append(elemento)
        return conjuntoResultado

    def disjuntos(self, conjunto):
        conjuntoResultado = []
        for i in self.conjunto:
            if i not in conjunto:
                conjuntoResultado.append(i)
            else:
                conjuntoResultado.append((i,'A'))
                
        for i in conjunto:
            if i not in self.conjunto:
                conjuntoResultado.append(i)
            else:
                conjuntoResultado.append((i,'B'))
                
        return conjuntoResultado

    def conuntoPartes(self):
        conjuntoResult = []
        tamanhoConjunto = len(self.conjunto)
        for x in range(tamanhoConjunto):
            for i in itertools.combinations(self.conjunto, x):
                conjuntoResult.append(i)
        return conjuntoResult


a = Conjunto()
a.adicionar('a')
a.adicionar('b')
a.adicionar('c')
a.adicionar('d')

                
print(a.conuntoPartes())



















    
