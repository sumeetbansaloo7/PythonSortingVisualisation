import time


def helper(array, drawArray, sleeptime):
    mergesort(array, 0, len(array)-1, drawArray, sleeptime)


def mergesort(data, left, right, drawArray, sleeptime):
    if left < right:
        middle = (left + right) // 2
        mergesort(data, left, middle, drawArray, sleeptime)
        mergesort(data, middle+1, right, drawArray, sleeptime)
        merge(data, left, middle, right, drawArray, sleeptime)


def merge(data, left, middle, right, drawArray, sleeptime):
    drawArray(data, getColorArray(len(data), left, middle, right))
    time.sleep(sleeptime)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawArray(data, ["green" if x >= left and x <=
                     right else "white" for x in range(len(data))])
    time.sleep(sleeptime)


def getColorArray(length, left, middle, right):
    cols = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                cols.append("yellow")
            else:
                cols.append("blue")
        else:
            cols.append("grey")

    return cols
