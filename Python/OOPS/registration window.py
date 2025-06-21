
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Registration")
win.geometry("1000x800")

frame = LabelFrame(win, text="Registration")
frame.pack()

name = Label(frame, text="Name:").grid(row=0, column=0)
ent_n = Entry(frame)
ent_n.grid(row=0, column=1)

f_name = Label(frame, text="Father's Name:").grid(row=1, column=0)
ent_f = Entry(frame)
ent_f.grid(row=1, column=1)

erp = Label(frame, text="ERP ID:").grid(row=2, column=0)
ent_e = Entry(frame)
ent_e.grid(row=2, column=1)

roll = Label(frame, text="Roll No.").grid(row=3, column=0)
ent_r = Entry(frame)
ent_r.grid(row=3, column=1)

branch = Label(frame, text="Branch:").grid(row=4, column=0)
br = Listbox(frame)
br.insert(1, "CSE")
br.insert(2, "IOT")
br.insert(3, "DS")
br.insert(4, "AI")
br.grid(row=4, column=1)

subject_widgets = []

def clear():
    global subject_widgets
    for widget in subject_widgets:
        widget.destroy()
    subject_widgets.clear()

def sem1():
    clear()
    global subject_widgets

    sub1 = Checkbutton(frame, text="Eng Mathematics-I")
    sub1.grid(row=6, column=1)
    subject_widgets.append(sub1)

    sub2 = Checkbutton(frame, text="Eng Physics")
    sub2.grid(row=6, column=2)
    subject_widgets.append(sub2)

    sub3 = Checkbutton(frame, text="Design Thinking")
    sub3.grid(row=6, column=3)
    subject_widgets.append(sub3)

    sub4 = Checkbutton(frame, text="COI")
    sub4.grid(row=6, column=4)
    subject_widgets.append(sub4)

def sem2():
    clear()
    global subject_widgets

    sub1 = Checkbutton(frame, text="Eng Mathematics-II")
    sub1.grid(row=6, column=1)
    subject_widgets.append(sub1)

    sub2 = Checkbutton(frame, text="BEEE")
    sub2.grid(row=6, column=2)
    subject_widgets.append(sub2)

    sub3 = Checkbutton(frame, text="Discrete Str")
    sub3.grid(row=6, column=3)
    subject_widgets.append(sub3)

    sub4 = Checkbutton(frame, text="Japanese")
    sub4.grid(row=6, column=4)
    subject_widgets.append(sub4)

sem = Label(frame, text="Semester").grid(row=5, column=0)
rad_var = IntVar()
rad1 = Radiobutton(frame, text="1st", variable=rad_var, value=1, command=sem1)
rad1.grid(row=5, column=1)
rad2 = Radiobutton(frame, text="2nd", variable=rad_var, value=2, command=sem2)
rad2.grid(row=5, column=2)

sub = Label(frame, text="Subjects").grid(row=6, column=0)

def cancel():
    messagebox.showinfo("Alert", "Fill Again")
    ent_n.delete(0, END)
    ent_f.delete(0, END)
    ent_e.delete(0, END)
    ent_r.delete(0, END)

def submit():
    messagebox.showinfo("Alert", "You have successfully registered")
    ent_n.delete(0, END)
    ent_f.delete(0, END)
    ent_e.delete(0, END)
    ent_r.delete(0, END)

but1 = Button(frame, text="Cancel", command=cancel)
but1.grid(row=7, column=0)
but2 = Button(frame, text="Submit", command=submit)
but2.grid(row=7, column=1)

win.mainloop()
