'''
from tkinter import *
roof = Tk()
roof.title("CSE")
roof.geometry("800x200")
roof.mainloop()
'''



'''
from tkinter import *
win =  Tk()
win.title("Input")
#win.attributes('-fullscreen', True)    #full screen
win.geometry("800x400")
win.config(bg = "yellow")

label = Label(win, text = "USER").grid(row = 0, column = 0)    #Label widgets
#label.config(bg = "red", fg="black")
#label.pack(padx = 50, pady= 50)
label1 = Label(win, text = "PASSWORD").grid(row = 1, column = 1)
#label1.pack(padx = 50, pady = 60)
#label.grid(row = 0, column = 0)    #placing the labels inside the grid
#label1.grid(row = 1, column = 1)
win.mainloop()
'''



#button widgets

'''
from tkinter import *
win =  Tk()
win.title("Input")
win.geometry("800x400")
win.config(bg = "yellow")
def xyz():
    label = Label(win, text = "Hello Python Class")
    label.pack()
button = Button(win, text = "submit", command = xyz)
button.pack()
win.mainloop()
'''



#button click counter
'''
from tkinter import *
root = Tk()
root.title("Button counter")
root.geometry("750x450")
counter = 0

def show():
    global counter
    global mylabel
    global button
    counter += 1
    mylabel.config(text = f"You clicked {counter} times")
    if counter >= 10:
        button.config(state = DISABLED)
        mylabel.config(text = "You clicked 10 times, button disabled")

mylabel = Label(root, text = "No click more")
mylabel.pack()
button = Button(root, text = "Click Me", command = show)
button.pack()

root.mainloop()
'''



#entry widgets

#to get data from entry widgets
'''
from tkinter import *
win = Tk()
win.title("Entry widgets")
win.geometry("750x650")

ent = Entry(win, bg = 'pink', fg = 'red')
ent.pack()
ent.insert(0, "Enter your name")

def show():
    x = ent.get()    #get method
    label = Label(win, text = x)
    label.pack()
    ent.delete(0, END)     #delete data from desktop
    #ent.config(state = DISABLED)    #disable entry

button = Button(win, text = "Submit", command = show)
button.pack()
win.mainloop()
'''



#frame widget
'''
from tkinter import *
win = Tk()
win.title("Widgets")
win.geometry("750x650")

myframe = LabelFrame(win, text = "My Frame", padx = 50, pady = 50)
myframe.pack(padx = 50, pady = 50)
mylabel = Label(myframe, text = "This is label")
mylabel.pack()
button = Button(myframe, text = "Submit")
button.pack()

win.mainloop()
'''



#scale widget
'''
from tkinter import *
win = Tk()
win.title("Widgets")
win.geometry("750x650")

scale = Scale(win, from_ = 0, to = 100, orient = HORIZONTAL, font = 26)
scale.pack()

win.mainloop()
'''



#checkbutton
'''
from tkinter import *
win = Tk()
win.title("Widgets")
win.geometry("750x650")

check_var = BooleanVar()
check = Checkbutton(win, text = "Option1")
check.pack()
check1 = Checkbutton(win, text = "Option2")
check1.pack()
check2 = Checkbutton(win, text = "Option3")
check2.pack()

win.mainloop()
'''



#radio button
'''
from tkinter import *
win = Tk()
win.title("Widgets")
win.geometry("750x650")

radio_var = StringVar()
radio1 = Radiobutton(win, text = "Male", variable = radio_var, value = "Male")
radio1.pack()
radio2 = Radiobutton(win, text = "Female", variable = radio_var, value = "Female")
radio2.pack()

win.mainloop()
'''



#message box
'''
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Widgets")
win.geometry("750x650")

def click():
    messagebox.showinfo("Warning", "You have successfully registered")

label = Label(win, text = "Hello")
label.pack()
button = Button(win,text = "Submit", command = click)
button.pack()

win.mainloop()
'''



#list box
'''
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Widgets")
win.geometry("750x650")

lb = Listbox(win)
lb.insert(1, "A")
lb.insert(2, "B")
lb.insert(3, "C")
lb.insert(4, "D")
lb.insert(5, "E")
lb.pack()

win.mainloop()
'''



#close window button
'''
from tkinter import *
win = Tk()
win.title("Destroy window")
win.geometry("750x650")

def click():
    win.destroy()
    
button = Button(win, text = "cancel", command = click)
button.pack()
'''



#automatic window close timer
'''
from tkinter import *
win = Tk()
win.title("Destroy window")
win.geometry("750x650")

l = Label(win, text = "This window will close after 5 seconds")
l.pack()
win.after(5000, lambda:win.destroy())
'''



#choose color
'''
from tkinter import *
from tkinter import colorchooser
win = Tk()
win.geometry("750x650")

def choose():
    color = colorchooser.askcolor(title = "Choose a color")
    
button = Button(win, text = 'Select color', command = choose)
button.pack()

win.mainloop()
'''



#digital watch
'''
from tkinter import *
import time
root = Tk()
root.geometry("500x125")
root.config(bg = "black")

def update():
    clock.config(text = time.strftime("%I:%M:%S"))
    clock.after(1000,update)
    
clock = Label(root, bg = "black", fg = "white", font = ('arial',72,'bold'))
clock.pack()
update()

root.mainloop()
'''



#canvas
'''
from tkinter import *
root = Tk()
root.title("Draw different shape")

canvas = Canvas(root, width = 400, height = 400)
canvas.pack()

canvas.create_line(0,0,200,100)

canvas.create_rectangle(50,50,200,200, fill = "green")

canvas.create_oval(100,120,250,270, fill = "yellow")

root.mainloop()
'''




#calculate sum
'''
from tkinter import *
win = Tk()
win.geometry("560x450")
def click():
    num1 = float(ent1.get())
    num2 = float(ent2.get())
    total = num1 + num2
    lb.config(text=f"Sum:{total}")
    
lb1 = Label(win, text = "num1:")
lb1.grid(row=0, column=0, padx=5, pady=5)
lb2 = Label(win, text = "num2:")
lb2.grid(row=1, column=0, padx=5, pady=5)

ent1 = Entry(win)
ent1.grid(row=0, column=1, padx=5, pady=5)
ent2 = Entry(win)
ent2.grid(row=1, column=1, padx=5, pady=5)

b = Button(win, text="Total Sum", command = click)
b.grid(row=2, column=0, columnspan=2, padx=5)

lb = Label(win, text= "Sum:")
lb.grid(row=3, columnspan=2, pady=5)
'''




#spinbox

from tkinter import *
win = Tk()
win.geometry("560x450")
spin = Spinbox(win, from_=0, to=10)
spin.pack()














































