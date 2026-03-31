from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Cisterian Number Generator")
root.resizable(False, False)

WIDTH = 400
HEIGHT = 600

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='lightblue')
canvas.pack(anchor=CENTER, expand=True)

Label(root, text="Enter a Number (1-9999)", font=("Arial", 12)).pack(pady=10)
entry = Text(root, height=1, width=4)
entry.pack()
Button(root, text="Enter", height=1, command=lambda: draw(int(entry.get("1.0", "end-1c")))).pack(pady=10)

def limit_text(event):
    """Prevent entering more than the allowed limit."""
    max_chars = 4
    text = entry.get("1.0", "end-1c")  # Get text excluding last newline
    if len(text) >= max_chars and event.keysym not in ("BackSpace", "Delete"):
        return "break"  # Prevent further input

entry.bind("<KeyPress>", limit_text)

# variables

SIZE = 100
CENTER = (WIDTH/2, HEIGHT/2*0.8)
WEIGHT = 15
COLOR = "black"

def add(tuple1, addend):
    if isinstance(addend, tuple):
        a = tuple1[0] + addend[0]
        b = tuple1[1] + addend[1]
    elif isinstance(addend, (int, float)):
        a = tuple1[0] + addend
        b = tuple1[1] + addend
    return ((a, b))

def subtract(tuple1, subtrahend):
    if isinstance(subtrahend, tuple):
        a = tuple1[0] - subtrahend[0]
        b = tuple1[1] - subtrahend[1]
    elif isinstance(subtrahend, (int, float)):
        a = tuple1[0] - subtrahend
        b = tuple1[1] - subtrahend
    return ((a, b))

def multiply(tuple1, factor):
    if isinstance(factor, tuple):
        a = tuple1[0] * factor[0]
        b = tuple1[1] * factor[1]
    elif isinstance(factor, (int, float)):
        a = tuple1[0] * factor
        b = tuple1[1] * factor
    return ((a, b))

def divide(tuple1, divisor):
    if isinstance(divisor, tuple):
        a = tuple1[0] / divisor[0]
        b = tuple1[1] / divisor[1]
    elif isinstance(divisor, (int, float)):
        a = tuple1[0] / divisor
        b = tuple1[1] / divisor
    return ((a, b))

#             TLeft, TRight, BRight, BLeft
pos = [(0, -1.5), (1, -1.5), (1, -0.5), (0, -0.5)]

coords = [
    [pos[0], pos[1]],                #1
    [pos[3], pos[2]],                #2
    [pos[0], pos[2]],                #3
    [pos[3], pos[1]],                #4
    [pos[0], pos[1], pos[3]],        #5
    [pos[1], pos[2]],                #6
    [pos[0], pos[1], pos[2]],        #7
    [pos[3], pos[2], pos[1]],        #8
    [pos[0], pos[1], pos[2], pos[3]] #9
]

def scale(coord: tuple, size: int, center: tuple = (0, 0)):
    coord = multiply(coord, size)
    coord = add(coord, center)
    return coord

def shape(num: int, mult: tuple = (1, 1)):
    for i in range(len(coords[num-1])-1):
        canvas.create_line(scale(multiply(coords[num-1][i], mult), SIZE, CENTER),
                           scale(multiply(coords[num-1][i+1], mult), SIZE, CENTER),
                           fill=COLOR, width=WEIGHT, capstyle="round")

def draw(num):
    canvas.delete("all")
    entry.delete("1.0", END)

    canvas.create_text(WIDTH/2, HEIGHT/10*8.5, text=str(num), font=("Arial", 64, "bold"))

    canvas.create_line(scale((0, -1.5), SIZE, CENTER),
                       scale((0, 1.5), SIZE, CENTER),
                       fill=COLOR, width=WEIGHT, capstyle="round")
    
    count = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    temp = num
    for i in range(len(str(temp))):
        if num % 10 != 0:
            shape(int(num%10), count[i])
        num /= 10

root.mainloop()