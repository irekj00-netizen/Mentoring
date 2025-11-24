import numpy as np
from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2

# pic_path = r"C:\Repozytoria\Mentoring\Image_6.png"
pic_path = r"C:\Repozytoria\Mentoring\kot_2.png"

def show_pic(picture):
    plt.imshow(picture)
    plt.axis('off')
    plt.show()

def npie_1():
    picture = np.array(img.imread(pic_path))
    picture_mono = picture[:, :, 2]
    mono_min = np.min(picture_mono)
    mono_max = np.max(picture_mono)
    picture_int = (picture_mono - mono_min) / (mono_max - mono_min) * 255
    return picture_mono, picture_int

def npie_2(picture):
    letter_C = picture[97:137, 138:175]
    return letter_C

def npie_3(picture, x, y):
    letter_C = picture[y-16: y+24, x-18: x+19]
    return letter_C

def npie_4(picture):
    return np.sum(picture)

def npie_5(picture):
    picture_bw = np.where(picture <= 127, 0, 255)
    return picture_bw

def npie_6_4(picture):
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    edges_x = edges_y = np.full((np.shape(picture)[0], np.shape(picture)[1]), 0)
    for i in range(1, np.shape(picture)[1] - 2):
        for j in range(1, np.shape(picture)[0] - 2):
            edges_x[j, i] = np.sum(picture[0+j:3+j, 0+i:3+i] * Gx)
            edges_y[j, i] = np.sum(picture[0+j:3+j, 0+i:3+i] * Gy)
    edges_x = (edges_x - np.min(edges_x)) / (np.max(edges_x) - np.min(edges_x)) * 255
    edges_y = (edges_y - np.min(edges_y)) / (np.max(edges_y) - np.min(edges_y)) * 255
    return edges_x, edges_y

def npie_6_6(picture):
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    edges = np.full((np.shape(picture)[0], np.shape(picture)[1]), 0)
    for i in range(1, np.shape(picture)[1] - 2):
        for j in range(1, np.shape(picture)[0] - 2):
            edges[j, i] = np.sqrt(np.square(np.sum(picture[0+j:3+j, 0+i:3+i] * Gx)) +
                                  np.square(np.sum(picture[0+j:3+j, 0+i:3+i] * Gy)))
    edges = (edges - np.min(edges)) / (np.max(edges) - np.min(edges)) * 255
    return edges

def npie_7(picture):
    Gx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    Gy = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    edges = np.full((np.shape(picture)[0], np.shape(picture)[1]), 0)
    for i in range(1, np.shape(picture)[1] - 2):
        for j in range(1, np.shape(picture)[0] - 2):
            edges[j, i] = np.sqrt(np.square(np.sum(picture[0+j:3+j, 0+i:3+i] * Gx)) +
                                  np.square(np.sum(picture[0+j:3+j, 0+i:3+i] * Gy)))
    edges = (edges - np.min(edges)) / (np.max(edges) - np.min(edges)) * 255
    return edges

# show_pic(npie_1()[1])
# show_pic(npie_2(npie_1()[0]))
# show_pic(npie_3(npie_1()[1], 156, 113))
# print(npie_4(npie_1()[0]), npie_4(npie_1()[1]))
show_pic(npie_5(npie_1()[1]))
# show_pic(npie_6_4(npie_1()[1])[1])
# show_pic(npie_6_6(npie_1()[1]))
# show_pic(npie_7(npie_1()[1]))