from tkinter import *

win = Tk()
win.geometry('400x689')
win.minsize(width=400, height=689)
win.maxsize(width=400, height=689)
win.title('Calculator - Basic')
win.iconbitmap("C:\\Users\\Akash\\Downloads\\Calculator-icon.ico")

scvalue = StringVar()
scvalue.set("")
ent = Entry(win, textvariable=scvalue ,font='Arial 19 bold', borderwidth=3, relief=SUNKEN)
ent.pack(padx=10, pady=10, ipadx=44, ipady=18)

def click(event):
    text = event.widget.cget("text")
    print(text)

    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(ent.get())
        scvalue.set(value)
        ent.update()

    elif text == 'C':
        scvalue.set(" ")
        ent.update()
    else:
        scvalue.set(scvalue.get() + text)
        ent.update()



# Frame 1
f = Frame(win, bg='grey')
f.pack()
btn = Button(f, text='9', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='8', font='Arial 15 bold')
btn.pack(padx=15, pady=1, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='7', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

# Frame 2
f = Frame(win, bg='grey')
f.pack()
btn = Button(f, text='6', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='5', font='Arial 15 bold')
btn.pack(padx=15, pady=1, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='4', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

# Frame 3
f = Frame(win, bg='grey')
f.pack()
btn = Button(f, text='3', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='2', font='Arial 15 bold')
btn.pack(padx=15, pady=1, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='1', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

# Frame 4
f = Frame(win, bg='grey')
f.pack()
btn = Button(f, text='0', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=33, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='+', font='Arial 15 bold')
btn.pack(padx=15, pady=1, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='-', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=32, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

# Frame 5
f = Frame(win, bg='grey')
f.pack()
btn = Button(f, text='*', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=33, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='/', font='Arial 15 bold')
btn.pack(padx=15, pady=1, ipadx=33, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='=', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=33, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

# Frame 6
f = Frame(win, bg='grey')
f.pack()
btn = Button(f, text='%', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=30, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='^', font='Arial 15 bold')
btn.pack(padx=15, pady=1, ipadx=30, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)

btn = Button(f, text='C', font='Arial 15 bold')
btn.pack(padx=15, pady=10, ipadx=30, ipady=18,side=LEFT)
btn.bind("<Button-1>", click)



win.mainloop()