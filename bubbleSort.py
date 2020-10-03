import time


def bubblesort(array, drawArray, sleeptime):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                drawArray(array, ["green" if x == j or x ==
                                  j+1 else "red" for x in range(len(array))])
                time.sleep(sleeptime)
    drawArray(array, ['green' for x in range(len(array))])
