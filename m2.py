def m2_1():
    słownik = {}
    słownik2 = dict()
    return słownik, słownik2

def m2_2():
    słownik = {"imię": "Wiesio2", "gatunek": "kot", "kolor": "czarny"}
    return słownik

def m2_3(słownik):
    słownik['lubi'] = 'spać'
    return słownik

def m2_4(słownik):
    słownik['lubi'] = 'jeść'
    return słownik

def m2_5(słownik):
    del słownik['lubi']
    return słownik

def m2_6(słownik, klucz):
    if klucz in słownik:
        return 'Jest'
    else:
        return 'Nie ma'

def m2_7(słownik, klucz):
    return słownik[klucz]

def m2_8(słownik, klucz):
    return słownik.get(klucz, 'brak klucza')

def m2_9(słownik):
    return słownik.keys()

def m2_10(słownik):
    return słownik.values()

def m2_11(słownik):
    return słownik

def m2_12(słownik):
    return len(słownik)

def m2_13(słownik):
    słownik.clear()
    return słownik

def m2_15(słownik):
    return słownik, słownik

def m2_16(słownik1, słownik2):
    return słownik1 | słownik2

def m2_17(lista1, lista2):
    return dict[lista1, lista2]

def m2_18(słownik):
    return {k: "Wartość domyślna" if v == None else v for (k, v) in słownik.items()}

def T1(n):
    print(n)
    if n == 0:
        return
    T1(n - 1)


# print(m2_14({'imię': 'Wiesio2', 'gatunek': 'kot', 'kolor': 'czarny', 'lubi': 'spać'}))
# print(m2_17(('a', 1), ('b', 2)))
print(m2_18({1: None, 2: "Dwa", 3: "Trzy"}))
# T1(5)