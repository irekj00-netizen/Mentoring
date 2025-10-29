import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2

def npi_1_pil():
    obraz = Image.open(r"C:\Users\irekj\Documents\Python\Mentoring\Image_6.png")
    return obraz

def npi_1_mpl():
    obraz = img.imread(r"C:\Users\irekj\Documents\Python\Mentoring\Image_6.png")
    return obraz

def npi_1_ocv():
    obraz = cv2.imread(r"C:\Users\irekj\Documents\Python\Mentoring\Image_6.png")
    return obraz

def npi_2a_pil(obraz):
    obraz.show()

def npi_2a_mpl(obraz):
    plt.imshow(obraz)
    plt.axis('off')
    plt.show()

def npi_2a_mpl_gray(obraz):
    obraz = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
    plt.imshow(obraz, cmap='gray')
    plt.axis('off')
    plt.show()

def npi_2a_ocv(obraz):
    cv2.imshow("Obraz", obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def npi_2b_pil(obraz):
    return obraz.format, obraz.size, type(obraz.getextrema()[0][0]), obraz.getextrema()

def npi_2b_mpl(obraz):
    return obraz.shape

def npi_2b_ocv(obraz):
    return obraz.shape, obraz[0], obraz[0][1]

def npi_3a_pil(obraz):
    obrazR = np.array(obraz)
    obrazG = np.array(obraz)
    obrazB = np.array(obraz)
    obrazR[:, :, (1,2)] = 0
    obrazG[:, :, (0,2)] = 0
    obrazB[:, :, (0,1)] = 0
    return Image.fromarray(obrazR), Image.fromarray(obrazG), Image.fromarray(obrazB)

def npi_3a_mpl(obraz):
    obrazR = obraz.copy()
    obrazG = obraz.copy()
    obrazB = obraz.copy()
    obrazR[:, :, (1,2)] = 0
    obrazG[:, :, (0,2)] = 0
    obrazB[:, :, (0,1)] = 0
    return obrazR, obrazG, obrazB

def npi_3a_ocv(obraz):
    obrazB = obraz.copy()
    obrazR = obraz.copy()
    obrazG = obraz.copy()
    obrazB[:, :, (1,2)] = 0
    obrazR[:, :, (0,1)] = 0
    obrazG[:, :, (0,2)] = 0
    return obrazR, obrazG, obrazB

# npi_2a_pil(npi_1_pil())
# npi_2a_mpl(npi_1_mpl())
# npi_2a_ocv(npi_1_ocv())
# print(npi_2b_pil(npi_1_pil()))
# print(npi_2b_mpl(npi_1_mpl()))
# print(npi_2b_ocv(npi_1_ocv()))
# print(npi_3a_pil(npi_1_pil()))
# npi_3a_mpl(npi_1_mpl())
# npi_3a_ocv(npi_1_ocv())
#
# for i in range(0,3):
#     npi_2a_pil(npi_3a_pil(npi_1_pil())[i])
#
# for i in range(0,3):
#     npi_2a_mpl(npi_3a_mpl(npi_1_mpl())[i])

for i in range(0,3):
    npi_2a_mpl_gray(npi_3a_mpl(npi_1_mpl())[i])

# for i in range(0,3):
#     npi_2a_ocv(npi_3a_ocv(npi_1_ocv())[i])