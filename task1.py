#! python3
""" 
Create a binary converter. Recall that binary is a system of counting based on powers of 2.
00000001 = 1    00000010 = 2    00001110 = 14
Create a converter that will convert binary to decimal or decimal to binary using the interface shown in task1.png Use the shell that 
has been started in task1.py. This is an incomplete program.  You will need to add onto it, but you should not change any of the commands that are already here
Use assignment_test.py to test your functions
"""
import tkinter as tk
from tkinter import *
import math
win=tk.Tk()
titleLabel = Label(win, text = "Binary/Decimal Converter!")
state = []
for i in range(1,9):
    state.append( IntVar() )

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    decimal = 0
    if binary[0] == 1:
        decimal = decimal + 128
    if binary[1] == 1:
        decimal = decimal + 64
    if binary[2] == 1:
        decimal = decimal + 32
    if binary[3] == 1:
        decimal = decimal + 16
    if binary[4] == 1:
        decimal = decimal + 8
    if binary[5] == 1:
        decimal = decimal + 4
    if binary[6] == 1:
        decimal = decimal + 2
    if binary[7] == 1:
        decimal = decimal + 1
    return decimal 
def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    num = int(decimal)
    value8 = 0
    value7 = 0
    value6 = 0
    value5 = 0
    value4 = 0
    value3 = 0
    value2 = 0
    value1 = 0
    if num >= 128:
        value8 = 1
        num = num - 128
    if num >= 64:
        value7 = 1
        num = num - 64
    if num >= 32:
        value6 = 1
        num = num - 32
    if num >= 16:
        value5 = 1
        num = num - 16
    if num >= 8:
        value4 = 1
        num = num - 8
    if num >=4:
        value3 = 1
        num = num - 4
    if num >= 2:
        value2 = 1
        num = num -2
    if num >= 1:
        value1 = 1
        num = num - 1
    binary = [value8, value7, value6, value5, value4, value3, value2, value1]
    return binary
def get_binary():
    # function should read the entry widget and generate an integer which will be used as an input
    #parameter for decimal to binary and the result updated in the 8 checkboxes
    decimal = entryBox.get()
    binary = decimal_to_binary(decimal)
    state[8].set(binary[0])
    state[7].set(binary[1])
    state[6].set(binary[2])
    state[5].set(binary[3])
    state[4].set(binary[4])
    state[3].set(binary[5])
    state[2].set(binary[6])
    state[1].set(binary[7])
def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated in the entry box
    binary = []
    for i in range(1,9):
        binary.append(state[i].get)
    decimal = binary_to_decimal(binary)
    blank.set(decimal)
blank = StringVar()
blank.set("")
cbs = []
for i in range(1,9):
    cbs.append( Checkbutton(win, variable = state[i]))
entryBox = Entry (win, textvariable = blank)
b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)
titleLabel.grid(row = 1, column = 2, columnspan = 6)
w1.grid(row = 2, column = 1)
w2.grid(row = 2, column = 2)
w3.grid(row = 2, column = 3)
w4.grid(row = 2, column = 4)
w5.grid(row = 2, column = 5)
w6.grid(row = 2, column = 6)
w7.grid(row = 2, column = 7)
w8.grid(row = 2, column = 8)
b1.grid(row = 3, column = 1, columnspan = 4)
b2.grid(row = 3, column = 5, columnspan = 4)
entryBox.grid(row = 4, column = 2, columnspan = 6)

win.mainloop()