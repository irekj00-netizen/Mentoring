def m1_1():
    lista=[i for i in range(1, 101)]
    return lista

def m1_2():
    lista = [i for i in range(1, 101, 2)]
    return lista

def m1_3():
    lista = [-i for i in range(1, 101)]
    return lista

def m1_4():
    lista = [-i for i in range(1, 101, 3)]
    return lista

def m1_5():
    lista = [101 - i for i in range(1, 101)]
    return lista

def m1_6():
    lista = [i for i in range(1000, 9, -10)]
    return lista

def m1_7():
    lista = [i for i in range(1, 101) if i % 3 == 0]
    return lista

def m1_8():
    lista = [i for i in range(1, 101) if i % 2 == 0]
    return lista

def m1_9():
    lista = [[j + i - 1 for j in range(1, 9)] for i in range(1, 9)]
    return lista

def m1_10():
    lista = [i * i for i in range(1, 11)]
    return lista

def m1_11():
    lista = [i for i in range(1, 11) if i != 3 and i != 7]
    return lista

def m1_12():
    lista = [0 for i in range(100)]
    return lista

def m1_14():
    lista = list(range(101))
    return lista

def m1_15(lista):
    return lista[-3]

def m1_16(lista):
    lista[8] = 13
    return lista

def m1_17(lista):
    if 10 in lista:
        return("Yes!")
    else:
        return("No!")

def m1_18(lista):
    return len([True for i in lista if i == 5])

def m1_19(lista):
    lst_srt = lista[:]
    lst_rev = lista[:]
    lst_srt.sort()
    lst_rev.sort(reverse=True)
    return lst_srt, lst_rev

def m1_20(lista):
    return min(lista), max(lista)

def m1_21(lista):
    return sum(lista)/len(lista)

def m1_22(lista):
    return sum(lista)

def m1_23(lista):
    lista.reverse()
    return lista

def m1_24(lista):
    return len(lista)

def m1_25(lista):
    połowa = len(lista) // 2
    lista_1 = lista[:połowa]
    lista_2 = lista[połowa:]
    return lista_1, lista_2

def m1_26(lista):
    del lista[-3]
    return lista

def m1_27(lista):
    lista2 = []
    for i in range(len(lista)):
        if i % 2 == 1:
            lista2.append(lista[i])
    return lista2

def m1_28(lista):
    lista2 = []
    for i in lista:
        lista2.append(i ** 2)
    return lista2

def m1_29(lista):
    return lista.index(max(lista))

def m1_30(lista):
    for i in range(lista.count(4)):
        lista.remove(4)
    return lista

def m1_31(lista):
    licznik = 0
    for i in lista:
        if i > 7:
            licznik += 1
    return licznik

def m1_32(lista):
    lista[4], lista[-1] = lista[-1], lista[4]
    return lista

def m1_33(lista):
    maks2 = min(lista)
    for i in lista:
        if i > maks2 and i < max(lista):
            maks2 = i
    return maks2

def m1_34(lista):
    lista_powt = []
    for i in lista:
        if lista.count(i) > 1 and i not in lista_powt:
            lista_powt.append(i)
    return lista_powt

def m1_35(lista):
    lista_unik = [i for i in lista if lista.count(i) == 1]
    return lista_unik

def m1_36(lista):
    for i in range(len(lista)//2):
        lista[i], lista[len(lista)-1-i] = lista[len(lista)-1-i], lista[i]
    return lista

def m1_37(lista):
    for i in range(len(lista)):
        if lista[i] > 5:
            lista[i] = True
    return lista

def m1_38(lista):
    suma=0
    for i in lista:
        if i % 2 == 1:
            suma += i
    return suma

def m1_39(lista):
    suma=0
    for i in range(len(lista)):
        if i % 2 == 0:
            suma += lista[i]
    return suma

def m1_40(lista):
    max_wyst = 0
    for i in lista:
        if lista.count(i) > max_wyst:
            liczba = i
            max_wyst = lista.count(i)
    return liczba

def m1_42(lista):
    return lista[-3:]

def m1_43(lista):
    return lista[1:-1]

def m1_44(lista):
    return lista[3:7]

def m1_45(lista):
    return lista[::2]

def m1_46(lista):
    return lista[-1::-1]

def m1_47(lista):
    return lista[-1::-2]

def m1_48(lista):
    lista[0:3] = [10, 11, 12]
    return lista

def m1_49(lista):
    lista[-1] = 999
    return lista

def m1_50(lista):
    lista = []
    return lista[:]

def m1_51(lista):
    lista = lista[2:5] + lista[2:5]
    return lista

def m1_52(lista):
    lista2 = [lista[i] + lista [abs(i-8)] for i in range(1, 8)]
    return lista2

def m1_53(macierz):
    wiersz_1 = ""
    for i in range(0, 3):
        wiersz_1 = wiersz_1 + str(macierz[i][0]) + ","
    return wiersz_1[:-1]

def m1_55(n):
    for i in range(1, n + 2):
        for j in range(1, i):
            print(j, end=" ")
        print("")

def m1_56(n):
    for i in range(1, n + 1):
        for j in range(1, i):
            print(j, end=" ")
        print("")
    for i in range(n + 1, 1, -1):
        for j in range(1, i):
            print(j, end=" ")
        print("")

def m1_57(lista):
    zmiany = 0
    for i in range(1, len(lista)):
        if lista[i] - lista[i - 1]:
            zmiany += 1
    return zmiany

def m1_58(lista):
    return list(enumerate(lista))

# print(m1_40([1, 2, 4, 5, 4, 3, 2, 5, 1, 10, 7, 5, 3, 4, 5, 1, 12, 3]))
print(m1_58(['a', 'b', 'c', 'd']))