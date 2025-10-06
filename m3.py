def m3_3():
    return {"Wiesiu2": {"Wiek": 4, "Gatunek": "Kot", "Odgłos": "miau", "Nogi": 3}, \
             "Łysek": {"Wiek": 15, "Gatunek": "Koń", "Odgłos": "ihaaa", "Nogi": 4}, \
             "Pucio": {"Wiek": 1, "Gatunek": "Cykada", "Odgłos": "cyk cyk", "Nogi": 6}}

def m3_4(słownik, imię):
    return imię, słownik[imię]["Nogi"]

def m3_5(słownik):
    słownik["Makarena"] = {"Wiek": 7, "Gatunek": "Stonga", "Odgłos": "tup tup", "Nogi": 100}
    return słownik

def m3_6(słownik):
    for i in słownik.keys():
        print(i, ":", słownik[i])

def m3_7(słownik):
    wartości = list(słownik.values())
    wartości.sort()
    return wartości

# słownik2 = {'e': 5, 'c': 3, 'a': 1, 'f': 0, 'b': 2, 'd':1}
#
# posort = list(słownik2.items())
# posort.sort(key = lambda x: x[1])
# słownik2 = dict(posort)
# słownik2
#
# #7.2
# słownik2 = {'e': 5, 'c': 3, 'a': 1, 'f': 0, 'b': 2, 'd': 1}
#
# lista = list(zip(słownik2.values(), słownik2.keys()))
# lista.sort()
# lista
#
#
# #8
# N = int(input("Podaj N:"))
# słownikN = {i:i**2 for i in range(1,N+1)}
# słownikN
#
# #9
# słownik2 = {'e': 5, 'c': 3, 'a': 1, 'f': 0, 'b': 2, 'd':1}
# suma = 0
# for i in słownik2.values():
#   suma += i
# suma
#
#
# #10
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = d1.copy()
# for key, value in d2.items():
#     d3[key] = d1.get(key,0) + d2.get(key,0)
# d3
#
# #11
# tekst = "Grzegorz Brzęczyszczykiewicz"
# słownik = {i:tekst.count(i) for i in tekst}
# słownik
#
# #12
# #zdanie = "Za piętnaście trzecia jestem ogolony, bo golę się wieczorem, śniadanie jadam na kolację, więc tylko wstaję i wychodzę."
# zdanie = "sto jeden sto dwa sto trzy sto cztery"
# słowa = zdanie.split()
# licznik_słów = {}
# for i in słowa:
#     licznik_słów[i] = licznik_słów.get(i,0) + 1
# licznik_słów

def m3_13(słownik):
    return all(słownik[i] == 12 for i in słownik)

def m3_14(słownik):
    for i in poziomy.items():
        print(i)
    if isinstance(poziomy["a"], dict):
        print("!")
    return "!"

def m3_29(słowo):
    if len(słowo) <= 1:
        return słowo
    return słowo[-1] + m3_29(słowo[:-1])

# print(m3_3())
# print(m3_4(m3_3(),"Wiesiu2"))
print(m3_7({'e': 5, 'c': 3, 'a': 1, 'f': 0, 'b': 2, 'd':1}))