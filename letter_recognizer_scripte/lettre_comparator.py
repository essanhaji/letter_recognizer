import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from PIL import Image
from my_modul import clear
from math import ceil, sqrt
from emnist import list_datasets
from emnist import extract_training_samples


class Letter_Comparator:

    def __init__(self):
        pass

    # desply images in one figure
    def disply_list_of_images(self, image_list):
        plt.figure(figsize=(10, 10))
        i = 1
        for image in image_list:
            nbr = ceil(sqrt(len(image_list)))
            plt.subplot(nbr, nbr, i)
            plt.imshow(image.image_color, plt.cm.binary)  
            i += 1
        plt.show()


if __name__ == "__main__":

    clear()

    letter_comparator = Letter_Comparator()
    
    # test
    # letter_comparator.disply_list_of_images()