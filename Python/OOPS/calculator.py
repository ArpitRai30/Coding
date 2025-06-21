from tkinter import *
win = Tk()
win.title("Calculator")
win.geometry("300x400")

frame = LabelFrame(win, width=200, height=300)
frame.pack(padx=50, pady=50)

L=[]

def n7():
    ent.insert(END, 7)
    L.append(7)

def n8():
    ent.insert(END, 8)
    L.append(8)

def n9():
    ent.insert(END, 9)
    L.append(9)

def div():
    ent.insert(END, '/')
    L.append('/')

def n4():
    ent.insert(END, 4)
    L.append(4)

def n5():
    ent.insert(END, 5)
    L.append(5)

def n6():
    ent.insert(END, 6)
    L.append(6)

def mul():
    ent.insert(END, '*')
    L.append('*')

def n1():
    ent.insert(END, 1)
    L.append(1)

def n2():
    ent.insert(END, 2)
    L.append(2)

def n3():
    ent.insert(END, 3)
    L.append(3)

def sub():
    ent.insert(END, '-')
    L.append('-')

def deci():
    ent.insert(END, '.')
    L.append('.')

def n0():
    ent.insert(END, 0)
    L.append(0)

def add():
    ent.insert(END, '+')
    L.append('+')

def clr():
    ent.delete(END)

def ac():
    ent.delete(0, END)

def eq():
    n1 = L[0]
    n2 = L[2]
    op = L[1]
    if op == '/':
        ent.delete(0, END)
        ent.insert(END, n1/n2)
    elif op == '-':
        ent.delete(0, END)
        ent.insert(END,n1-n2)
    elif op == '+':
        ent.delete(0, END)
        ent.insert(END,n1+n2)
    elif op == '*':
        ent.delete(0, END)
        ent.insert(END,n1*n2)



ent = Entry(frame)
ent.grid(row=0, column=0, columnspan=4)

b7 = Button(frame, text="7", command=n7)
b7.grid(row=1, column=0)

b8 = Button(frame, text="8", command=n8)
b8.grid(row=1, column=1)

b9 = Button(frame, text="9", command=n9)
b9.grid(row=1, column=2)

b_div = Button(frame, text="/", command=div)
b_div.grid(row=1, column=3)

b_clr = Button(frame, text="CLR", command=clr)
b_clr.grid(row=1, column=4)

b4 = Button(frame, text="4", command=n4)
b4.grid(row=2, column=0)

b5 = Button(frame, text="5", command=n5)
b5.grid(row=2, column=1)

b6 = Button(frame, text="6", command=n6)
b6.grid(row=2, column=2)

b_mul = Button(frame, text="*", command=mul)
b_mul.grid(row=2, column=3)

b_ac = Button(frame, text="AC", command=ac)
b_ac.grid(row=2, column=4)

b1 = Button(frame, text="1", command=n1)
b1.grid(row=3, column=0)

b2 = Button(frame, text="2", command=n2)
b2.grid(row=3, column=1)

b3 = Button(frame, text="3", command=n3)
b3.grid(row=3, column=2)

b_sub = Button(frame, text="-", command=sub)
b_sub.grid(row=3, column=3)

b_deci = Button(frame, text=".", command=deci)
b_deci.grid(row=4, column=0)

b0 = Button(frame, text="0", command=n0)
b0.grid(row=4, column=1)

b_eq = Button(frame, text="=", command=eq)
b_eq.grid(row=4, column=2)

b_add = Button(frame, text="+", command=add)
b_add.grid(row=4, column=3)


win.mainloop()