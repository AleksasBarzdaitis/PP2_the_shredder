def image_size_det(height, width):
    eligible_divisors = False
    while not eligible_divisors:
        common_divisors = []
        for i in range(10, min(height, width), 2):
            if height % i == 0 and width % i == 0:
                common_divisors.append(i)
        if common_divisors[-1] < 40:
            height -= 10
        else:
            eligible_divisors = True
    return common_divisors, height, width