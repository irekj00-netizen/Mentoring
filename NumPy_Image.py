import numpy as np
from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2

ścieżka = r"C:\Users\irekj\Documents\Python\Mentoring\Image_6.png"

def npi_1a_pil():
    obraz = Image.open(ścieżka)
    return obraz

def npi_1b_mpl():
    obraz = img.imread(ścieżka)
    return obraz

def npi_1c_ocv():
    obraz = cv2.imread(ścieżka)
    return obraz

def npi_2(obraz):
    plt.imshow(obraz)
    plt.axis('off')
    plt.show()

def npi_2a(obraz1, obraz2, obraz3):
    plt.subplot(1, 3, 1)
    plt.imshow(obraz1)
    plt.axis('off')
    plt.subplot(1, 3, 2)
    plt.imshow(obraz2)
    plt.axis('off')
    plt.subplot(1, 3, 3)
    plt.imshow(obraz3)
    plt.axis('off')
    plt.show()

def npi_2b(obraz1, obraz2, obraz3):
    return "Pillow:", type(obraz1), "MatPlotLib:", type(obraz2), "OpenCV:", type(obraz3)

def npi_2c(obraz1, obraz2, obraz3):
    obraz1 = np.array(obraz1)
    obraz2 = np.array(obraz2)
    obraz3 = np.array(obraz3)
    return "Pillow:", obraz1.shape, obraz1.dtype, obraz1.min(), obraz1.max(),\
           "MatPlotLib:", obraz2.shape, obraz2.dtype, obraz2.min(), obraz2.max(),\
           "OpenCV:", obraz3.shape, obraz3.dtype, obraz3.min(), obraz3.max()

def npi_3a(obraz):
    obrazR, obrazG, obrazB = obraz[::, ::, 0], obraz[::, ::, 1], obraz[::, ::, 2]
    return obrazR, obrazG, obrazB

def npi_3b(obraz):
    print(obraz.shape)
    plt.imshow(obraz)
    plt.axis('off')
    plt.show()
    plt.imshow(obraz, cmap='gray')
    plt.axis('off')
    plt.show()

def npi_4a():
    print("Kolory są zamienione, bo OpenCV używa BRG zamiast RGB.")

def npi_4b(obraz):
    obraz_rgb=cv2.cvtColor(obraz, cv2.COLOR_BGR2RGB)
    cv2.imshow("Obraz", obraz_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def npi_5(obraz):
    obrazR = obraz[::, ::, 0]
    obrazG = obraz[::, ::, 1]
    obrazB = obraz[::, ::, 2]
    obrazBW = (obrazR*.299+obrazG*.587+obrazB*.114)
    obrazBW2 = (obrazR*.2126+obrazG*.7152+obrazB*.0722)
    plt.subplot(1, 2, 1)
    plt.imshow(obrazBW[::,::], cmap='gray')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(obrazBW2[::, ::], cmap='gray')
    plt.axis('off')
    plt.show()
    # return obraz

def npi_6(obraz):
    negatyw = 255 - obraz
    print(type(negatyw))
    plt.imshow(negatyw)
    plt.axis('off')
    plt.show()

def npi_7(obraz):
    negatyw = 1 - obraz
    print(type(negatyw))
    plt.imshow(negatyw)
    plt.axis('off')
    plt.show()

# npi_2a(npi_1a_pil(), npi_1b_mpl(), npi_1c_ocv())
# print(npi_2b(npi_1a_pil(), npi_1b_mpl(), npi_1c_ocv()))
# print(npi_2c(npi_1a_pil(), npi_1b_mpl(), npi_1c_ocv()))
# for i in range(0,3):
#     npi_3b(npi_3a(npi_1b_mpl())[i])
# npi_5(npi_1b_mpl())
# npi_6(npi_1c_ocv())
npi_7(npi_1b_mpl())
