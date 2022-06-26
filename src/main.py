import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt

img = image.imread('src\images\dog1.jpg')

split_freq = 40
cropped = img[0:1120, 0:1600]
print(cropped.shape)
# lst=[]
#
lst = np.hsplit(cropped, split_freq)
indexes1 = []
indexes2 = []

for i in range(split_freq):
    if i % 2 == 0:
        indexes1.append(i)
    else:
        indexes2.append(i)
arr = np.array(lst)

test1 = arr[indexes1]
test2 = arr[indexes2]

breed1 = np.concatenate((test1), axis=1)
breed2 = np.concatenate((test2), axis=1)

twobreeds = np.concatenate((breed1, breed2), axis=1)

lst_of_vertical_split = np.vsplit(twobreeds, split_freq)
arr1 = np.array(lst_of_vertical_split)

test3 = arr1[indexes1]
test4 = arr1[indexes2]

breed3 = np.concatenate(test3, axis=0)
breed4 = np.concatenate(test4, axis=0)

fourbreeds = np.concatenate((breed3, breed4), axis=1)


print(twobreeds.shape)

# print(breed1.shape)
# print(breed1.shape)


# revers = lst[::-1]
# one = lst[0:1]
# plt.imshow(np.concatenate((test4), axis=0))
# breed2 = plt.imshow(np.concatenate((test2), axis=1))

plt.imshow(fourbreeds)

print(fourbreeds.shape)

plt.show()

# print(type(lst))