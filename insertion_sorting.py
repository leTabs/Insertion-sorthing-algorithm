# Insertion sorting algorithm

def insertion_sorting(array):
    if array[0]>array[1]:
        array[0], array[1] = array[1], array[0]

    # making sure that the first and the second items in the array
    # are sorting correctly in comparison with each other.

    for i in range(2, len(array)):

        # looping for each item starting from the third, meaning the index 2.

        for r in range(len(array[:i]), 0, -1):
            # looping backwards from the current item.

            if array[i] < array[r-1]:
                # and comparing it with each previous item
                # if it's smaller...
                array[i], array[r-1] = array[r-1], array[i]
                # swap their places
                i-=1 # decrement the i so that the comparison continue happen.

        # and on to the next item
    return array

# testing
random_array = [-10, -5, 0, 3, -2, 8, -6, 1, -4, 7]
