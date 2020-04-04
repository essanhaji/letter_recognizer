from correlation import compute_correlation_similarity_score
from sorensen import compute_sorensen_similarity_score
from jaccard import compute_jaccard_similarity_score
from lettre_comparator import Letter_Comparator
from emnist import extract_training_samples
from emnist import list_datasets
from my_modul import clear
from letter import Letter
import numpy as np
import time

start = time.time()

# to clear the console
clear()


images, labels = extract_training_samples('letters')

# print(images.shape)
# print(labels.shape)

# to minimize the data set to accelerate test
# images = images[0:1000]
# labels = labels[0:1000]

# print(images.shape)
# print(labels.shape)

# create Letter_Comparator class instance
my_comparator = Letter_Comparator()
# create array of pictures class instance
letters_array = np.array([])

for i in range(len(images)):
    letter = Letter(i, labels[i], images[i])
    letters_array = np.append(letters_array, letter)

# print(pictures_array[9].show())

# the the request image
initial_letter = letters_array[2]

for letter in letters_array:
    # you can change compute_correlation_similarity_score 
    # by
    # compute_jaccard_similarity_score
    # or 
    # compute_sorensen_similarity_score
    letter.temps = compute_correlation_similarity_score(initial_letter.vector, letter.vector)

print("<< {} >>".format(initial_letter.label))

letters_array.sort()

# letters_array = letters_array[::1]

my_comparator.disply_list_of_images(letters_array[0:20])

print("Execution time : {} S".format((time.time() - start)))
