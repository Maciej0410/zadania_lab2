from math import *

x = (input(u"Podaj liczbę z której obliczę pierwiastek: "))
x=int(x)
try:
        wynik = sqrt(x)
        print(wynik)
except ValueError:
        print(u"Podano ujemną liczbę")