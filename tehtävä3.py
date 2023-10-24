class Auto:
    def __init__(self, rkt, hn):
        self.rkt = rkt
        self.hn = int(hn)
        self.nopeus = 0
        self.kuljettu = 2000

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.hn:
            self.nopeus = self.hn
        elif self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tunti):
        self.kuljettu += self.nopeus * tunti

    def __str__(self):
        return f'{self.rkt}, {self.hn}, {self.nopeus}, {self.kuljettu}'

auto = Auto("ABC-123", "142")
nopeus = int(input("Anna nopeus "))
Nopeus = auto.kiihdytä(nopeus)
aika = float(input("Anna kuljettu aika "))
auto.kulje(aika)
print(auto)