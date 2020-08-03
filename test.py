import tkinter as tk

def changeit():
	l.config(text="Not the start")

top = tk.Tk()

l = tk.Label(top, text="Start")
l.pack()

b = tk.Button(top, width=25, text="Add", command=changeit)
b.pack()

top.mainloop()