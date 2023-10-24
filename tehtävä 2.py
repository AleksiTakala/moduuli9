class Auto:
    def __init__(self, rkt, hn):
        self.rkt = rkt
        self.hn = int(hn)
        self.nopeus = 0
        self.kuljettu = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.hn:
            self.nopeus = self.hn
        elif self.nopeus < 0:
            self.nopeus = 0


    def __str__(self):
        return f'{self.rkt}, {self.hn}, {self.nopeus}, {self.kuljettu}'

auto = Auto("ABC-123", "142")
print("Auto kiihdyttää 30km/h", auto.kiihdytä(30))
print(auto)
print("Auto kiihdyttää 70km/h",auto.kiihdytä(70))
print(auto)
print("Auto kiihdyttää 50km/h",auto.kiihdytä(50))
print(auto)
auto.kiihdytä(-200)
print(auto)
