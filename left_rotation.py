def rotLeft(a, d):
    # instantiate a new list with same length as input
    rotated = [None] * len(a)

    for i in range(len(a)):
        # new index caluclated by subtracting num of rotations by length of array
        # then add current index and modulo length of array for final index
        rotated[(i + (len(a) - d)) % len(a)] = a[i]

    return rotated


if __name__ == '__main__':
    
    print(rotLeft([1, 2, 3, 4, 5], 4))
    print(rotLeft([1, 2, 3, 4, 5], 7))