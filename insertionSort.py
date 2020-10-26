import time


def insertionsort(array, drawArray, sleeptime):
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]
        drawArray(array, colours(len(array), i))
        time.sleep(sleeptime)
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            drawArray(array, colours(len(array), i, j))
            time.sleep(sleeptime)
            j -= 1
        array[j + 1] = key
        drawArray(array, colours(len(array), i))
        time.sleep(sleeptime)


def colours(length, key, j=0):
    cols = []
    for i in range(length):
        if i == key:
            cols.append('blue')
        elif i < key:
            cols.append('green')
        else:
            cols.append("yellow")

    if j != 0:
        cols[j] = 'red'
    return cols
