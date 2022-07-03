import numpy as np
import yaml
from matplotlib import image
import shredder_actions as sa

# Loading image from config file
with open('.\config\config.yml', 'r') as config:
    options = yaml.safe_load(config)['options']
    loaded_image = options['images']
img = image.imread(loaded_image)

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

# Setting up The Shredder
# Loading config file to get size of shreds (shredded and glued image quality)
with open('.\config\config.yml', 'r') as config:
    options = yaml.safe_load(config)['options']
    quality_selected = options['display_quality']

print(f'Shredded image quality selected: {quality_selected}')

if quality_selected == 'low':
    shred_freq = common_divisors[0]
elif quality_selected == 'medium':
    shred_freq = common_divisors[len(common_divisors) // 2]
elif quality_selected == 'high':
    shred_freq = common_divisors[-1]

print(f'Cropped image shape: {cropped_img.shape}')
print(f'Common divisors: {common_divisors}')
print(f'Shred frequency: {shred_freq}')

titles = ['Original image', 'Cropped image',
          'Result of first shredding, splitting and gluing',
          'Final result of shredding, splitting and gluing']

# Display original size and cropped image
sa.display_image(img, titles[0], 5)
sa.display_image(cropped_img, titles[1], 5)

# Shredding vertically, splitting, gluing and displaying cropped image
first_shred = sa.shredding_splitting_gluing(cropped_img, shred_freq, 1, np.hsplit)
sa.display_image(first_shred, titles[2], 10)

# Shredding horizontally, splitting, gluing and displaying glued image
second_shred = sa.shredding_splitting_gluing(first_shred, shred_freq, 0, np.vsplit)
sa.display_image(second_shred, titles[3], 10)

print(f'Final shape after shredding and gluing: {second_shred.shape}')