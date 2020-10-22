import time


def bubblesort(array, drawArray, sleeptime):
    length = len(array)
    for i in range(length-1):
        for j in range(length-1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                drawArray(array, colours(length, j, j+1))
                time.sleep(sleeptime)
    # drawArray(array, ['green' for x in range(len(array))])


def colours(length, smaller, bigger):
    cols = []
    for i in range(length):
        if i == smaller:
            cols.append('blue')
        elif i == bigger:
            cols.append('green')
        else:
            cols.append("red")
    return cols

# test_array = [49, 4, 72, 9, 34, 123, 17]

# bubblesort(test_array,10,10)
# print(test_array)
