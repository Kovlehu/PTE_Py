class Teglalap:
    def __init__(self, a, b): # innen sorban megy le, mindig inittel kezdd
        self.a = a
        self.b = b

    def terulet(self):
        return self.a * self.b

    def kerulet(self):
        return 2 * (self.a + self.b)

    def teruletkiir(self):
        print("A terulet:", self.terulet())

    def keruletkiir(self):
        print("A kerulet:", self.kerulet())

class Negyzet(Teglalap): # oroklodes (zarojelben)
    def __init__(self, a):
        super().__init__(a, a) # ososztaly (Teglalap) initjet hivom meg

class SzinesNegyzet(Negyzet):
    def __init__(self, a, szin):
        super().__init__(a)
        self.szin = szin

    def mennyi_festek(self):
        print(self.terulet(), "cm2", self.szin, "festek kell")

t1 = Teglalap(10, 20)
print(t1.a)
print(t1.b)
# print(t1.terulet()) # metodus, kell az extra zarojel
t1.teruletkiir()
t1.keruletkiir()

n = Negyzet(10)
n.teruletkiir()

m = SzinesNegyzet(20, "piros")
m.teruletkiir()
m.mennyi_festek()