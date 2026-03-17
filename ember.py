class Ember:
    def __init__(self, nev, kor, jegyek): #self kotelezo
        self.nev = nev
        self.kor = kor
        self.jegyek = jegyek # alakzatok utan

    def bemutatkozas(self):
        print("Szia,", self.nev, "vagyok", self.kor, "eves")

# Ez elott az alakzatokat nezd at

    def jegyet_kap(self, jegy):
        self.jegyek.append(jegy)

    def atlag(self):
        return sum(self.jegyek / len(self.jegyek))

    def atlag_kiir(self):
        print("A tanulo atlaga: ", self.atlag())

    def bukik_e(self):
    # True, ha az atlag < 1.5, kulonben False
       return self.atlag() < 1.5

    def javitott_e(self):
    # True, ha az utolso 3 jegy atlaga jobb, mint az osszatlag
        return (sum(self.jegyek[-3:] / 3) > self.atlag())

# ember1 = Ember("Jozsi", 22) # elejehez
# print(ember1.nev)
# print(ember1.kor)
# ember1.bemutatkozas()

ember2 = Ember("Anna", 19, [2, 1, 1, 1]) # jegyes feladathoz
print(ember2.bukik_e())
print(ember2.atlag_kiir())
print(ember2.javitott_e())