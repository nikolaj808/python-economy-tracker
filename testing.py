import os
import sys
import tkinter as tk
from tkinter import filedialog, Text
from datetime import date
date = date.today()

#######################################################################

if os.path.exists("expenses.txt") == False:
    fp = open("expenses.txt", "x")
    fp.close()

if os.path.exists("previousdate.txt") == False:
    fp = open("previousdate.txt", "x")
    fp.close()

def getCurrent():
    fp = open("expenses.txt", "r")
    current = fp.read()
    fp.close()
    if current == '':
        fp = open("expenses.txt", "w")
        current = 0
        fp.write(str(current) + "\n")
    return float(current)

root = tk.Tk()
root.config(background='#052F5F')
e1 = tk.Entry(root)
value = 0

def addToCurrent(amount):
    fp = open("expenses.txt", "r")
    current = fp.read()
    fp.close()
    if current == '':
        fp = open("expenses.txt", "w")
        current = float(0) + float(amount)
        fp.write(str(current) + "\n")
        fp.close()
    else:
        fp = open("expenses.txt", "w")
        current = float(current) + float(amount)
        fp.write(str(current) + "\n")
        fp.close()
    #print("Previous previous date was: " + str(getPreviousDate()))
    #setPreviousDate(getDateNumber())
    #print("New previous date set to: " + str(getDateNumber()))
    return

#######################################################################

def add_field():
	e1.grid(row=3, column=1)

def add_expense(event):
	value = float(e1.get())
	e1.delete(0, 'end')
	e1.grid_forget()
	addToCurrent(value)
	current_label.config(text=getCurrent())
	
tk.Label(root, text="Expenses Manager", font=("Roboto", 42), background='#052F5F', fg='#06A77D').grid(row=0, column=1)
tk.Label(root, text="Current Month", font=("Roboto", 28), background='#052F5F', fg='#06A77D').grid(row=1, column=1)
current_label = tk.Label(root, text=getCurrent(), font=("Roboto", 24), background='#052F5F', fg='#D5C67A')
current_label.grid(row=2, column=1)

add_button = tk.Button(root, width=25, text="Add", command=add_field, background='#005377', fg='#F1A208')
add_button.grid(row=4, column=0, padx=(10, 10), pady=(10,1.5))

check_button = tk.Button(root, width=25, text="Check", command=root.quit, background='#005377', fg='#F1A208')
check_button.grid(row=4, column=1, padx=(10, 10), pady=(10,1.5))

edit_button = tk.Button(root, width=25, text="Edit", command=root.quit, background='#005377', fg='#F1A208')
edit_button.grid(row=4, column=2, padx=(10, 10), pady=(10,1.5))

delete_button = tk.Button(root, width=25, text="Delete", command=root.quit, background='#005377', fg='#F1A208')
delete_button.grid(row=5, column=0, padx=(10, 10), pady=(10,1.5))

quit_button = tk.Button(root, width=25, text="Quit", command=root.quit, background='#005377', fg='#F1A208')
quit_button.grid(row=5, column=2, padx=(10, 10), pady=(10,1.5))

toggle_button = tk.Button(root, width=25, text="Toggle Show", command=root.quit, background='#005377', fg='#F1A208')
toggle_button.grid(row=5, column=1, padx=(10, 10), pady=(10, 1.5))

e1.bind('<Return>', add_expense)
root.mainloop()
