import time


def selectionsort(array, drawArray, sleeptime):
    for i in range(len(array)):
        drawArray(array, colours(len(array), i, 0))
        time.sleep(sleeptime)
        min_index = i
        for j in range(i+1, len(array)):
            drawArray(array, colours(len(array), i, j, min_index))
            time.sleep(sleeptime)
            if array[min_index] > array[j]:
                min_index = j
                drawArray(array, colours(len(array), i, j, min_index))
                time.sleep(sleeptime)
        array[i], array[min_index] = array[min_index], array[i]
        # drawArray(array, colourswhileswapping(len(array), i, min_index))
        # time.sleep(sleeptime)
        drawArray(array, colourswhileswapping(len(array), min_index, i))
        time.sleep(sleeptime)


def colours(length, curr, j, min_index=0):
    cols = ["yellow" for i in range(length)]
    cols[curr] = "red"
    if(j != 0):
        cols[j] = "blue"
    if curr != min_index and min_index != 0:
        cols[min_index] = "green"
    return cols


def colourswhileswapping(length, a, b):
    cols = ["yellow" for i in range(length)]
    cols[a] = "red"
    cols[b] = "green"
    return cols
