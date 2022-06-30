import numpy as np
from matplotlib import image
import operations as op

# Loading image
img = image.imread('images\dog1.jpg')
print(f'Original image shape: {img.shape}')

# Rounding image size to tens
original_img_height = img.shape[0]
original_img_width = img.shape[1]
rounded_img_height = (original_img_height // 10) * 10
rounded_img_width = (original_img_width // 10) * 10

# Determining nearest image size for eligible shred sizes for suitable image quality representation
eligible_divisors = False
while not eligible_divisors:
    common_divisors = []

    for i in range(10, min(rounded_img_height, rounded_img_width), 2):
        if rounded_img_height % i == 0 and rounded_img_width % i == 0:
            common_divisors.append(i)

    if common_divisors[-1] < 30:
        rounded_img_height -= 10
    else:
        eligible_divisors = True

# Cropping image to determined size
cropped_img = img[0:rounded_img_height, 0:rounded_img_width]

# Setting up shredding frequency
shred_freq = common_divisors[-1]

print(f'Cropped image shape: {cropped_img.shape}')
print(f'Common divisors: {common_divisors}')
print(f'Shred frequency: {shred_freq}')

titles = ['Original image', 'Cropped image',
          'Result of first shredding, splitting and gluing',
          'Final result of shredding, splitting and gluing']

# Display original size and cropped image
op.display_image(img, titles[0], 10)
op.display_image(cropped_img, titles[1], 10)

# Shredding, splitting, gluing and displaying cropped image
first_shred = op.shredding_splitting_gluing(cropped_img, shred_freq, 1, np.hsplit)
op.display_image(first_shred, titles[2], 10)

# Shredding, splitting, gluing and displaying glued image
second_shred = op.shredding_splitting_gluing(first_shred, shred_freq, 0, np.vsplit)
op.display_image(second_shred, titles[3], 10)

print(f'Final shape after shredding: {second_shred.shape}')