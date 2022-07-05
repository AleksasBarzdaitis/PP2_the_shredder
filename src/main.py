import numpy as np
import yaml
from matplotlib import image
import os
import shredder_actions as sa
import image_processing as ip
import shredder as sh
import dev_prints as dp

while os.getcwd().split('\\')[-1] != "PP2_the_shredder":
    os.chdir('..')

# Loading image from config file
with open('.\config\config.yml', 'r') as config:
    options = yaml.safe_load(config)['options']
    loaded_image = options['images']
img = image.imread(loaded_image)

# Loading display titles
with open('.\config\config.yml', 'r') as config:
    options = yaml.safe_load(config)['options']
    titles = options['titles']

# Rounding image size to tens
original_img_height = img.shape[0]
original_img_width = img.shape[1]
rounded_img_height = (original_img_height // 10) * 10
rounded_img_width = (original_img_width // 10) * 10

# Determining nearest image size for eligible shred sizes for suitable image quality representation
shred_sizes, height, width = ip.image_size_det(rounded_img_height, rounded_img_width)

# Cropping image to determined size
cropped_img = img[0:height, 0:width]

# Loading config file to get size of shreds (shredded and glued image quality)
with open('.\config\config.yml', 'r') as config:
    options = yaml.safe_load(config)['options']
    quality_selected = options['display_quality']

# Setting up The Shredder
shred_size = sh.shred_size(shred_sizes, quality_selected)

# Display original size and cropped image
sa.display_image(img, titles[0], 5)
sa.display_image(cropped_img, titles[1], 5)

# Shredding vertically, splitting, gluing and displaying cropped image
first_shred = sa.shredding_splitting_gluing(cropped_img, shred_size, 1, np.hsplit)
sa.display_image(first_shred, titles[2], 10)

# Shredding horizontally, splitting, gluing and displaying glued image
second_shred = sa.shredding_splitting_gluing(first_shred, shred_size, 0, np.vsplit)
sa.display_image(second_shred, titles[3], 10)

# dp.dev_log(img, quality_selected, cropped_img, shred_sizes, shred_size, second_shred)