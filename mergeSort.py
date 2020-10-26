import time


def helper(array, drawArray, sleeptime):
    mergesort(array, 0, len(array)-1, drawArray, sleeptime)


def mergesort(array, left, right, drawArray, sleeptime):
    if left < right:
        middle = (left + right) // 2
        mergesort(array, left, middle, drawArray, sleeptime)
        mergesort(array, middle+1, right, drawArray, sleeptime)
        merge(array, left, middle, right, drawArray, sleeptime)


def merge(array, left, middle, right, drawArray, sleeptime):
    drawArray(array, getColorArray(len(array), left, middle, right))
    time.sleep(sleeptime)

    leftpartion = array[left:middle+1]
    rightpartion = array[middle+1: right+1]

    l = 0
    r = 0

    for dataIdx in range(left, right+1):
        if l < len(leftpartion) and r < len(rightpartion):
            if leftpartion[l] <= rightpartion[r]:
                array[dataIdx] = leftpartion[l]
                l += 1
            else:
                array[dataIdx] = rightpartion[r]
                r += 1

        elif l < len(leftpartion):
            array[dataIdx] = leftpartion[l]
            l += 1
        else:
            array[dataIdx] = rightpartion[r]
            r += 1

    drawArray(array, ["green" if x >= left and x <=
                      right else "white" for x in range(len(array))])
    time.sleep(sleeptime)


def getColorArray(length, l, m, r):
    cols = []

    for i in range(length):
        if i >= l and i <= r:
            if i >= l and i <= m:
                cols.append("yellow")
            else:
                cols.append("blue")
        else:
            cols.append("grey")

    return cols
