import numpy as np
from matplotlib import pyplot as plt


def shredding_splitting_gluing(img, shred_freq, axis, func):
    # Creating a list of vertically or horizontally shredded image pieces and converting it to numpy array
    list_of_shredded_pieces = func(img, shred_freq)
    arr = np.array(list_of_shredded_pieces)
    # Creating a list of indexes for splitting shredded image pieces
    even_indexes = []
    odd_indexes = []
    for i in range(shred_freq):
        if i % 2 == 0:
            even_indexes.append(i)
        else:
            odd_indexes.append(i)
    # Splitting shredded image pieces to two
    image1_pieces = arr[even_indexes]
    image2_pieces = arr[odd_indexes]
    # "Gluing" split pieces into two images
    image1 = np.concatenate(image1_pieces, axis=axis)
    image2 = np.concatenate(image2_pieces, axis=axis)
    # "Gluing" two images into one
    image1_image2 = np.concatenate((image1, image2), axis=1)
    return image1_image2


def display_image(img, title, pause):
    plt.imshow(img)
    plt.title(title)
    plt.show(block=False)
    plt.pause(pause)