from m1 import *
from m2 import *
from m3 import *
from m4 import *
import unittest

print(m1_1()) #1

class TestLista(unittest.TestCase):
    def test_lista_ma_100_elementów(self):
        self.assertEqual(len(lista), 100, "Lista nie ma 100 elementów.")


# print (m1_20([1,2,3])) #2

# print (m1_49([1,2,3])) #3, 4

# print (m2_13({"Wiesio":"kot", "Pimpek":"pies"})) #5

# print (m2_16({1:2}, {3:4})) #6

# print (m3_13({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12})) #7
#
# print (m3_14({1:2})) #8

# print(m3_29("qwerty")) #9




