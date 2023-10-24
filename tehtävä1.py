class Auto:
    def __init__(self, rkt, hn):
        self.rkt = rkt
        self.hn = hn
        self.nopeus = 0
        self.kuljettu = 0

    def __str__(self):
        return f'{self.rkt}, {self.hn}, {self.nopeus}, {self.kuljettu}'

auto = Auto("ABC-123", "142 km/h")
print(auto)







