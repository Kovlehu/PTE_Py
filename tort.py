# dunder metodusok
# double under

class Tort:
    def __init__(self, szamlalo, nevezo):
        self.szamlalo = szamlalo
        self.nevezo = nevezo

        self.egyszerusit()

    def egyszerusit(self): # Ez dunderek utan kerult be (kiir nem)
        for i in range(min(self.szamlalo, self.nevezo), 1, -1):
            if self.szamlalo % i == 0 and self.nevezo % i == 0:
                self.szamlalo //= i
                self.nevezo //= i
                break

    def kiir(self):
        print(self.szamlalo, "/", self.nevezo)

# dunder metodusok

    def __str__(self):
        return str(self.szamlalo) + "/" + str(self.nevezo)

    def __float__(self):
        return self.szamlalo / self.nevezo

    def __int__(self):
        return self.szamlalo // self.nevezo

    def __mul__(self, other):
        if type(other) == str:
            other = int(other)
        if type(other) == int:
            return Tort(self.szamlalo * other, self.nevezo)
        elif type(other) == Tort:
            return Tort(
                self.szamlalo * other.szamlalo,
                self.nevezo * other.nevezo
            )

        def __eq__(self, other): # na itt nemtom mi van
            if type(other) == bool:
              return bool(self) == other
            if type(other) == float:
              return bool(self) == other
            if type(other) == str:
                szam, nev = other.split("/")
                return int(szam) / int(nev) == float(self)

tort1 = Tort(10, 8) # torteket csinalj magadnak, nezd meg mi mit csinal, en itt nagyon elvesztem

print(int(tort1 * 10 * Tort(2, 25)))
