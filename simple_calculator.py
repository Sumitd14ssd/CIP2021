import tkinter


# =========================================================================================
# Defined below are various functions for button operations
def button_click(number):
    current = displayWindow.get()
    displayWindow.delete(0, tkinter.END)
    displayWindow.insert(0, str(current) + str(number))


def button_clear():
    displayWindow.delete(0, tkinter.END)


def button_ops():
    first_number = displayWindow.get()
    global first_num
    first_num = float(first_number)
    displayWindow.delete(0, tkinter.END)


def button_add():
    button_ops()
    global math
    math = "addition"


def button_subtract():
    button_ops()
    global math
    math = "subtraction"


def button_multiply():
    button_ops()
    global math
    math = "multiplication"


def button_divide():
    button_ops()
    global math
    math = "division"


def button_equal():
    second_number = displayWindow.get()
    displayWindow.delete(0, tkinter.END)
    if math == "addition":
        displayWindow.insert(0, first_num + float(second_number))
    if math == "subtraction":
        displayWindow.insert(0, first_num - float(second_number))
    if math == "multiplication":
        displayWindow.insert(0, first_num * float(second_number))
    if math == "division":
        if second_number == '0':
            displayWindow.insert(0, 'NaN')
        else:
            displayWindow.insert(0, first_num / float(second_number))


# ===========================================================================================
# Global variables declaration
first_num = 0.0
math = None

keys = [[('CE', 1, button_clear)],
        [('7', 1, lambda: button_click(7)), ('8', 1, lambda: button_click(8)),
         ('9', 1, lambda: button_click(9)), ('+', 1, button_add)],
        [('4', 1, lambda: button_click(4)), ('5', 1, lambda: button_click(5)),
         ('6', 1, lambda: button_click(6)), ('-', 1, button_subtract)],
        [('1', 1, lambda: button_click(1)), ('2', 1, lambda: button_click(2)),
         ('3', 1, lambda: button_click(3)), ('*', 1, button_multiply)],
        [('0', 1, lambda: button_click(0)), ('=', 2, button_equal), ('/', 1, button_divide)],
        ]

# ============================================================================================
# Creating the 'Calculator' main window
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow['padx'] = 10
mainWindow['pady'] = 10

# Creating the display window where results are shown
displayWindow = tkinter.Entry(mainWindow, borderwidth=5)
displayWindow.grid(row=0, column=0, sticky='nsew', pady=8)

# Creating a frame for the keypad
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, pady=8)

# Populating the keypad using the for loop
row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0], padx=20, pady=10, command=key[2])\
            .grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.mainloop()
