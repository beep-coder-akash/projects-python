from tkinter import *
from tkinter import messagebox
win = Tk()
win.minsize(width=544, height=455)
win.maxsize(width=544, height=455)
win.title('To-Do List App')
win.iconbitmap("C:\\Users\\Akash\\Downloads\\to-do.ico")

# Function to define the workflow
def add():
    task = ent.get()
    if task != "":
        lb.insert(END, task)
        ent.delete(0, END)

def comp():
    selected = lb.curselection()
    task = lb.get(selected)
    lb.delete(selected)
    lb.insert(END, f"✔ {task}")

def dlt():
    try:
        selected = lb.curselection()
        lb.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please Select a Task")


# Label for top introduction
label = Label(win, text='Save Your Tasks', font='comicsansms 23 bold')
label.pack()

# List box for saving tasks
lb = Listbox(win, borderwidth=4, relief=SUNKEN, font='Arial 12 bold', bg='grey', fg='white')
lb.pack(ipadx=130, ipady=40)

# Entry box
ent = Entry(win, font='Arial 9 bold')
ent.pack(pady=10, ipadx=20, ipady=3)

# Buttons for save, add, delete tasks
btn1 = Button(win, padx=12, pady=8 ,text='Add', font='Arial 10 bold', command=add)
btn1.place(x=100, y=390)

btn2 = Button(win, padx=12, pady=8 ,text='Mark Completed', font='Arial 10 bold', command=comp)
btn2.place(x=200, y=390)

btn3 = Button(win, padx=12, pady=8 ,text='Delete', font='Arial 10 bold', command=dlt)
btn3.place(x=380, y=390)


win.mainloop()