import time


def partition(array, head, tail, drawArray, sleeptime):
    border = head
    pivot = array[tail]
    drawArray(array, colours(len(array), head, tail, border, border))
    time.sleep(sleeptime)
    for i in range(head, tail):
        if array[i] < pivot:
            drawArray(array, colours(len(array), head,
                                     tail, border, i, True))
            time.sleep(sleeptime)
            array[border], array[i] = array[i], array[border]
            border += 1
        drawArray(array, colours(len(array), head, tail, border, i))
        time.sleep(sleeptime)
    drawArray(array, colours(len(array), head, tail, border, tail, True))
    time.sleep(sleeptime)
    array[border], array[tail] = pivot, array[border]
    return border


def quicksort(array, head, tail, drawArray, sleeptime):
    if(head < tail):
        part_index = partition(array, head, tail, drawArray, sleeptime)
    #! left half
        quicksort(array, head, part_index-1, drawArray, sleeptime)
    #! right half
        quicksort(array, part_index+1, tail, drawArray, sleeptime)


def colours(length, head, tail, border, curr, whenswapping=False):
    cols = []
    for i in range(length):
        if i >= head and i <= tail:  # working half
            cols.append('yellow')
        else:  # half currently not working
            cols.append('gray')
        if i == tail:
            cols[i] = 'brown'
        elif i == border:
            cols[i] = 'red'
        elif i == curr:
            cols[i] = "blue"
        if whenswapping:
            if i == border or i == curr:
                cols[i] = 'green'
    return cols
# test_array = [49, 4, 72, 9, 34, 23, 17]

# quicksort(test_array, 0, len(test_array)-1, 10, 10)
# print(test_array)
