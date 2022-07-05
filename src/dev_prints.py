def dev_log(img, quality_selected, cropped_img, shred_sizes, shred_size, second_shred):
    print(f'Original image shape: {img.shape}')
    print(f'Shredded image quality selected: {quality_selected}')
    print(f'Cropped image shape: {cropped_img.shape}')
    print(f'Common divisors: {shred_sizes}')
    print(f'Shred frequency: {shred_size}')
    print(f'Final shape after shredding and gluing: {second_shred.shape}')