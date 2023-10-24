import random
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
    def kulje(self, tunti):
        self.kuljettu += self.nopeus * tunti

    def __str__(self):
        return f'{self.rkt}, {self.hn}, {self.nopeus}, {self.kuljettu}'
autolista = []
matkalista = []
for i in range(1):
    for i in range(10):
        i = i +1
        nopeuss = random.randint(100,200)
        aut = Auto("ABC-"+ str(i), nopeuss)
        aut.kiihdytä(nopeuss)
        aut.kulje(10)
        autolista.append(aut)
        aut.kuljettu += aut.kuljettu
        matkalista.append(aut.kuljettu)

print(matkalista)


