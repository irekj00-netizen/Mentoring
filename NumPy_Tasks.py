#1
import numpy as np
# from numpy.ma.core import count

def npt_2():
    tablica = np.array([i for i in range(1,11)])
    return tablica

def npt_3(tablica):
    return np.shape(tablica), tablica.dtype

def npt_4(wymiar):
    # return np.array([np.array([j+1 for j in range(i*wymiar, i*wymiar+wymiar)]) for i in range(0, wymiar)])
    return np.array([[j+1 for j in range(i*wymiar, i*wymiar+wymiar)] for i in range(0, wymiar)])

def npt_5():
    return np.zeros([10]), np.zeros([3,4])

def npt_6():
    return np.ones([10]), np.ones([5,4])

def npt_7():
    return np.arange(0, 22, 2)

def npt_8():
    return np.linspace(0,1,10)

def npt_9():
    return np.eye(4,4)

def npt_10():
    return np.array([np.random.randint(1,100) for _ in range(10)])

def npt_11(lista1, lista2):
    tabl1 = np.array(lista1)
    tabl2 = np.array(lista2)
    return tabl1 + tabl2, tabl1 - tabl2, tabl1 * tabl2, tabl1 / tabl2

def npt_12(lista):
    # return np.square(np.array(lista))
    return np.power(np.array(lista), [2, 2, 2])

def npt_13(lista):
    return np.average(lista), np.sum(lista), np.min(lista), np.max(lista)

def npt_14(lista):
    return np.sqrt(lista)

def npt_15a(p, k):
    arr = np.arange(p, k)
    return arr, arr[0], arr[2], arr[-1]

def npt_15b(p, k):
    return np.arange(p, k)[2:8]

def npt_15c(p, k):
    return np.arange(p, k)[-1::-1]

def npt_16a(lista):
    return np.array(lista)[0]

def npt_16b(lista):
    tablica = np.array(lista)
    return np.array([tablica[i][1] for i in range(0,3)])

def npt_16c(lista):
    tablica = np.array(lista)
    return np.array(tablica[1][2])

def npt_16d(lista):
    tablica = np.array(lista)
    indeksy = [i for i in np.argwhere(tablica>5)]
    return np.array([tablica[indeksy[i][0]][indeksy[i][1]] for i in range(0,4)])

def npt_17a(p, k):
    x = np.arange(p, k)
    return np.array([i for i in x if i % 3 == 0])

def npt_17b(p, k):
    x = np.arange(p, k)
    return np.array([99 if i > 10 else i for i in x])

def npt_17c(p, k):
    x = np.arange(p, k)
    return np.size([True for i in x if i<8])

def npt_17d(p, k):
    x = np.arange(p, k)
    return np.sum([i for i in x if i % 2 == 0])\

def npt_18a(tablica):
    return np.array([1 if i > 10 else i for i in tablica])

def npt_18b(tablica):
    return np.array([0 if i <= 10 else i for i in tablica])

def npt_18c(tablica):
    return np.array([0 if i <= 10 else 1 for i in tablica])

def npt_19():
    tablica = np.random.randint(low = 1, high = 100, size=(15))
    return np.array([i for i in tablica if i > np.average(tablica)])

def npt_20a(tablica):
    return [0 if i < 0 else i for i in tablica]

def npt_20b(tablica):
    return [5 if i > 5 else i for i in tablica]

def npt_21():
    return np.random.randint(low = 1, high = 10, size=(4, 4))

def npt_21a(tablica):
    wsp_np = np.where(tablica % 2 == 1) # tablica ze współrzędnymi liczb nieparzystych
    for i in range(0, np.size(wsp_np[0]-1)):
        tablica[wsp_np[0][i], wsp_np[1][i]] = -1
    return tablica

def npt_21b(tablica):
    wsp_p = np.where(tablica % 2 == 0) # tablica ze współrzędnymi liczb parzystych
    for i in range(0, np.size(wsp_p[0]-1)):
        tablica[wsp_p[0][i], wsp_p[1][i]] = 1
    return tablica

def npt_22(wymiar):
    tablica = np.array([np.array([j + 1 for j in range(i * wymiar, i * wymiar + wymiar)]) for i in range(0, wymiar)])
    return tablica

def npt_22a(tablica):
    return np.sum(tablica, axis=1), np.sum(tablica, axis=0)

def npt_22b(tablica):
    return np.max(tablica), np.min(tablica)

def npt_22c(tablica):
    return np.sum(tablica, axis=1)/3

def npt_23a(A, B):
    return np.add(A, B), np.subtract(A, B), np.multiply(A, B)

def npt_23b(A, B):
    return np.matmul(A, B)

def npt_23c(A):
    return np.matmul(np.linalg.inv(A), A)

def npt_24(n):
    return np.reshape([i+1 for i in range(n*n)], (4,4))

def npt_24a(A):
    return np.diag(A)

def npt_24b(A): # spróbować metodą z 24d
    return np.flip(A, axis=1)
    # return np.array([A[i][::-1] for i in range(0,4)])

def npt_24c(A):
    return np.flip(A, axis=0)

def npt_24d(A): # sprawdzić inne kombinacje
    A[[0, 3],:] = A[[3,0],:]
    return A

def npt_24e(A):
    return A.flatten()

def npt_25():
    A = np.array([np.random.randint(0,100) for i in range(0,10)])
    return A, (A - np.min(A))/(np.max(A) - np.min(A))

def npt_26():
    return np.random.rand(20)

def npt_26a(A):
    return np.array([np.average(A), np.median(A), np.var(A), np.std(A)])

def npt_26b(A):
    ens = 1
    for i in A:
        if ens - np.average(A) < ens:
            ens = i
    return A, np.average(A), ens



# print(npt_2())
# print(npt_3(npt_2()))
# print(npt_4(3))
# print(npt_5())
# print(npt_6())
# print(npt_7())
# print(npt_8())
# print(npt_9())
# print(npt_10())
# print(npt_11([1, 2, 3], [4, 5, 6]))
# print(npt_12([1, 2, 3]))
# print(npt_13([4, 5, 6]))
# print(npt_14([4, 5, 6]))
# print (npt_15a(10, 20))
# print (npt_15b(10, 20))
# print (npt_15c(10, 20))
# print(npt_16a([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(npt_16b([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(npt_16c([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(npt_16d([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print (npt_17a(1, 21))
# print (npt_17b(1, 21))
# print (npt_17c(1, 21))
# print (npt_17d(1, 21))
# print (npt_18a(np.arange(1, 21)))
# print (npt_18b(np.arange(1, 21)))
# print (npt_18c(np.arange(1, 21)))
# print (npt_19())
# print(npt_20a([3, -7, 0, 5, -2, 9]))
# print(npt_20b([3, -7, 0, 5, -2, 9]))
# print(npt_21())
# print(npt_21a(npt_21()))
# print(npt_21b(npt_21()))
# print(npt_22(3))
# print(npt_22a(npt_22(3)))
# print(npt_22b(npt_22(3)))
# print(npt_22c(npt_22(3)))
# print (npt_23a([[2, 4],[1,3]], [[5, 2],[3, 6]]))
# print (npt_23b([[2, 4],[1,3]], [[5, 2],[3, 6]]))
# print (npt_23c([[2, 4],[1,3]]))
# print (npt_24(4))
# print (npt_24a(npt_24(4)))
# print (npt_24b(npt_24(4)))
# print (npt_24c(npt_24(4)))
# print (npt_24d(npt_24(4)))
# print (npt_24e(npt_24(4)))
# print(npt_25())
# print(npt_26())
# print(npt_26a(npt_26()))
# print(npt_26b(npt_26()))
a = [[0,1,2],[3,4,5],[6,7,8]]
# a[0],a[-1] = a[-1],a[0]
print(a, a[0][-1])