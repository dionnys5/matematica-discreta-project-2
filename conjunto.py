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
        z = conjunto
        for i in self.conjunto:
            if i not in conjunto:
                elemento.append(i)
        return z

    def interseccao(self, conjunto):
        z = []
        for i in self.conjunto:
            if i in conjunto:
                z.append(i)
        return z

    def diferenca(self, conjunto):
        z = []
        for i in self.conjunto:
            if i not in conjunto:
                z.append(i)
        return z

    def complemento(self, conjunto):
        z = []
        for i in self.conjunto:
            if i not in conjunto:
                z.append(i)
        return z

##    def partes(self):
##        z = [None]
##        for i in self.conjunto:
##            z.append((i))
##        
##        
##

    def cartesiano(self, conjunto):
        z = []
        for i in self.conjunto:
            for j in conjunto:
                z.append((i,j))
        return z

    def disjuntos(self, conjunto):
        z = []
        for i in self.conjunto:
            if i not in conjunto:
                z.append(i)
            else:
                z.append((i,'A'))
                
        for i in conjunto:
            if i not in self.conjunto:
                z.append(i)
            else:
                z.append((i,'B'))
                
        return z

a = Conjunto()
a.adicionar(1)
a.adicionar(2)
a.adicionar(3)
a.adicionar(4)
print(a.conjunto)

print('*****************')

b = Conjunto()
b.adicionar(1)
b.adicionar(2)
b.adicionar(5)
b.adicionar(7)

#Impressão para teste de metodos

print(a.disjuntos(b.conjunto))
