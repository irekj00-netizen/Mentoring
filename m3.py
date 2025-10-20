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

def m3_8(n):
    return {i:i**2 for i in range(1,n+1)}

def m3_9(słownik):
    suma = 0
    for i in słownik.values():
        suma += i
    return suma

def m3_10(słownik1, słownik2):
    słownik3 = słownik1.copy()
    for key, value in słownik2.items():
        słownik3[key] = słownik1.get(key,0) + słownik2.get(key,0)
    return słownik3

def m3_11(tekst):
    słownik = {i:tekst.count(i) for i in tekst}
    return słownik

def m3_12(tekst):
    słowa = tekst.split()
    licznik = {}
    for i in słowa:
        licznik[i] = licznik.get(i,0) + 1
    return licznik

def m3_13(słownik):
    return all(słownik[i] == 12 for i in słownik)

def m3_14(słownik, licznik):
    max_licznik = licznik
    for i in słownik.items():
        print(słownik, licznik)
        if isinstance(i[1], dict):
            max_licznik = max(max_licznik, m3_14(i[1], licznik+1))
    return max_licznik

def m3_15(oceny):
    for k in oceny.keys():
        oceny[k] = min(oceny[k]+1, 5)
    return oceny

def m3_16(oceny):
    min_ocena = min(oceny.values())
    min_oceny = {}
    for k in oceny.keys():
        if oceny[k] == min_ocena:
            min_oceny[k] = min_ocena
    return min_oceny

def m3_17(oceny):
    oceny5 = {}
    for k in oceny.keys():
        if oceny[k] == 5:
            oceny5[k] = 5
    return oceny5

def m3_18(oceny):
    return sum(oceny.values())/len(oceny.values())

def m3_19(oceny):
    do_usunięcia = [k for k in oceny if oceny[k] <= 3]
    for k in do_usunięcia:
        oceny.pop(k)
    return oceny

def m3_20(oceny):
    return dict(sorted(oceny.items()))

def m3_21
# wg_nazwisk = {k.split()[1] + " " + k.split()[0]:students[k] for k in students}
# dict(sorted(wg_nazwisk.items()))
#
# #22
# nazwiska_i_oceny = {k.split()[1]: students[k] for k in students}
# nazwiska_i_oceny
#
# #23
# wg_ocen2 = [(students.get(k),k) for k in students]
# wg_ocen2.sort()
# for i in range(0,3):
#     print(wg_ocen2[i])
#
# #24
# students.update({"Adam Ondra": None})
# print(students)
# students = {k:students[k] for k in students if students[k] != None}
#
# students
#
# #25
# students.update({None:3})
# do_usunięcia = [k for k in students if k == None]
# for k in do_usunięcia:
#     students.pop(k)
# students
#
# #26
# students = {"Anna Kowalska": 5, "Celina Wiśniewska": 3, "Damian Wójcik": 2.5, "Iga Dąbrowska": 2, "Elżbieta Kamińska": 5,\
#             "Filip Zieliński": 4, "Gabriela Szymańska": 3, "Hubert Lewandowski": 5, "Jakub Kozłowski": 4, "Karolina Jankowska": 5,\
#              "Łukasz Mazur": 3.5,"Magdalena Krawczyk": 2, "Bartosz Nowak": 4.5, "Norbert Król": 4, "Oliwia Pawlak": 5}
#
# # oceny = []
# # for i in students.values():
# #    if oceny.count(i) == 0:
# #       oceny.append(i)
#
# # oceny = {v for v in students.values()}
# # {k:{v for v in students.keys() if students.get(v) == k} for k in oceny}
#
# {k:{v for v in students.keys() if students.get(v) == k} for k in {v for v in students.values()}}
#
#
#
# #27
# def liczby(N):
#   if N == 0:
#     return
#   print(N)
#   liczby(N-1)
#
# liczby(5)
#
# #28
# def liczby(k,N):
#   print(k)
#   if k == N:
#     return
#   liczby(k+1,N)
#
# liczby(1,5)

# def m3_29(słowo):
#     if len(słowo) <= 1:
#         return słowo
#     return słowo[-1] + m3_29(słowo[:-1])

# print(m3_3())
# print(m3_4(m3_3(),"Wiesiu2"))
# print(m3_7({'e': 5, 'c': 3, 'a': 1, 'f': 0, 'b': 2, 'd':1}))
# print(m3_8(7))
# print(m3_9({'e': 5, 'c': 3, 'a': 1, 'f': 0, 'b': 2, 'd':1}))
# print(m3_10({'a': 100, 'b': 200, 'c':300}, {'a': 300, 'b': 200, 'd':400}))
# print(m3_11("Grzegorz Brzęczyszczykiewicz"))
# print(m3_12("sto jeden sto dwa sto trzy sto cztery"))
# print(m3_13({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12, 'John Rib': 11}))
# print(m3_14({"a":{"b":{"c":"Dno"}, "d":"Muł"},"e":{"f": {"g":{"h":"Dno"}}}}, 0))
print(m3_20({"Anna Kowalska": 5, "Celina Wiśniewska": 3, "Damian Wójcik": 2.5, "Iga Dąbrowska": 2, "Elżbieta Kamińska": 5,\
            "Filip Zieliński": 4, "Gabriela Szymańska": 3, "Hubert Lewandowski": 5, "Jakub Kozłowski": 4, "Karolina Jankowska": 5,\
             "Łukasz Mazur": 3.5,"Magdalena Krawczyk": 2, "Bartosz Nowak": 4.5, "Norbert Król": 4, "Oliwia Pawlak": 5}))