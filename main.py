from tkinter import *
from tkinter import ttk
import random  # for creating new random array
from bubbleSort import bubblesort
from quickSort import quicksort

# variables
algoSelected = StringVar()
array = []


def Generate():
    global array
    print("algoSelected = " + algoSelected.get())
    minVal = int(minScale.get())
    maxVal = int(maxScale.get())
    size = int(sizeScale.get())
    array = []
    for i in range(size):
        array.append(random.randrange(minVal, maxVal+1))
    drawArray(array, ['red' for x in range(len(array))])


def drawArray(array, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 780
    x_width = canvas_width/(len(array)+1)
    offset = 25
    spacing = 10
    normalizedData = [i/max(array)for i in array]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width+offset+spacing
        y0 = canvas_height-height * 400
        # bottom right
        x1 = (i+1)*x_width+offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(array[i]))

    canvas.create_text(125, 30, text=algoSelected.get())
    root.update_idletasks()


def startAlgorithm():
    global array
    sleeptime = float(speedScale.get())
    if(algoSelected.get() == "Bubble Sort"):
        bubblesort(array, drawArray, sleeptime)
        drawArray(array, ['green' for x in range(len(array))])
    else:
        quicksort(array, 0, len(array)-1, drawArray, sleeptime)
        drawArray(array, ['green' for x in range(len(array))])


#! ui using tkinter
# window properties
root = Tk()
root.title("Sorting Visuallisation")
root.maxsize(900, 600)
root.config(bg="black")
# main ui and canvas for visualisation
UI_frame = Frame(root, width=900, height=200, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=800, height=500, bg="light blue")
canvas.grid(row=1, column=0, padx=10, pady=5)
# user interface
# first row
sizeScale = Scale(UI_frame, from_=5, to=50, length=150, digits=1,
                  resolution=0.2, orient=HORIZONTAL, label="Size of Array")
sizeScale.grid(row=0, column=1, padx=5, pady=5)
minScale = Scale(UI_frame, from_=0, to=50, length=150, digits=1,
                 resolution=0.2, orient=HORIZONTAL, label="Min Value")
minScale.grid(row=0, column=2, padx=5, pady=5)
maxScale = Scale(UI_frame, from_=50, to=200, length=150, digits=1,
                 resolution=0.2, orient=HORIZONTAL, label="Max Value")
maxScale.grid(row=0, column=3, padx=5, pady=5)
Button(UI_frame, text="Create Array", command=Generate,
       bg='red').grid(row=0, column=4, padx=5, pady=5)
# second row
Label(UI_frame, text="Algorithm: ", bg="grey").grid(
    row=1, column=0, padx=5, pady=5, sticky=W)
#! algos for sorting
algoMenu = ttk.Combobox(UI_frame, textvariable=algoSelected, values=[
                        "Bubble Sort", "Quick Sort"])
algoMenu.grid(row=1, column=1, padx=5, pady=5)
algoMenu.current(0)
speedScale = Scale(UI_frame, from_=0.1, to=1.0, length=150, digits=2,
                   resolution=0.1, orient=HORIZONTAL, label="Select Speed (seconds)")
speedScale.grid(row=1, column=2, padx=5, pady=5)
Button(UI_frame, text="Start Sorting", command=startAlgorithm,
       bg='red').grid(row=1, column=3, padx=5, pady=5)


root.mainloop()
