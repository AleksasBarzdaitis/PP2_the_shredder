def shred_size(shred_sizes, quality):
    if quality == 'low':
        return shred_sizes[0]
    elif quality == 'medium':
        return shred_sizes[len(shred_sizes) // 2]
    elif quality == 'high':
        return shred_sizes[-1]