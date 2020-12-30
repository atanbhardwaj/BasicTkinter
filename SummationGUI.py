from tkinter import *

window = Tk()


def summa():
    val1 = int(e1_value.get())
    return val1


def summa1():
    val2 = int(e2_value.get())
    return summa() + val2


def final_res():
    var = summa1()
    t1.insert(END, var)


b1 = Button(window, text="Enter value of a", command=summa)
# b1.pack()
b1.grid(row=0, column=0)

b2 = Button(window, text="Enter value of b", command=summa1)
b2.grid(row=1, column=0)

b3 = Button(window, text="Result", command=final_res)
b3.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=1, column=1)


t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=3)


window.mainloop()
