import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2

def npi_1_pil(): #PIL
    obraz = Image.open(r"C:\Users\irekj\Documents\Python\Mentoring\Image_6.png")
    return obraz

def npi_1_mpl(): #matplotlib
    obraz = img.imread(r"C:\Users\irekj\Documents\Python\Mentoring\Image_6.png")
    return obraz

def npi_1_ocv(): #OpenCV
    obraz = cv2.imread(r"C:\Users\irekj\Documents\Python\Mentoring\Image_6.png")#OpenCV
    return obraz

def npi_2a_pil(obraz):
    obraz.show()

def npi_2a_mpl(obraz):
    plt.imshow(obraz)
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
    obrazR[:, :, 1] *= 0
    obrazR[:, :, 2] *= 0
    obrazR = Image.fromarray(obrazR)
    obrazR.show()
    obrazG = np.array(obraz)
    obrazG[:, :, 0] *= 0
    obrazG[:, :, 2] *= 0
    obrazG = Image.fromarray(obrazG)
    obrazG.show()
    obrazB = np.array(obraz)
    obrazB[:, :, 0] *= 0
    obrazB[:, :, 1] *= 0
    obrazB = Image.fromarray(obrazB)
    obrazB.show()

def npi_3a_mpl(obraz):
    obrazR = obraz.copy()
    obrazG = obraz.copy()
    obrazB = obraz.copy()
    obrazR[::, ::, (1,2)] = 0
    plt.imshow(obrazR)
    plt.show()
    obrazG[::, ::, (0,2)] = 0
    plt.imshow(obrazG)
    plt.show()
    obrazB[::,::, (0,1)]=0
    plt.imshow(obrazB)
    plt.show()

def npi_3a_ocv(obraz):
    obrazR = obraz.copy()
    obrazG = obraz.copy()
    obrazB = obraz.copy()
    obrazR[:, :, (0,1)] = 0
    obrazG[:, :, (0,2)] = 0
    obrazB[:, :, (1,2)] = 0
    cv2.imshow("Red", obrazR)
    cv2.imshow("Green", obrazG)
    cv2.imshow("Blue", obrazB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# npi_2a_pil(npi_1_pil())
# npi_2a_mpl(npi_1_mpl())
# npi_2a_ocv(npi_1_ocv())
# print(npi_2b_pil(npi_1_pil()))
# print(npi_2b_mpl(npi_1_mpl()))
# print(npi_2b_ocv(npi_1_ocv()))
# npi_3a_pil(npi_1_pil())
# npi_3a_mpl(npi_1_mpl())
npi_3a_ocv(npi_1_ocv())