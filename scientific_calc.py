from tkinter import *
import math
from tkinter import messagebox

# Main window
win = Tk()
win.minsize(width=734, height=388)
win.maxsize(width=734, height=388)
win.title('Calculator - Scientific')

# Click function to use buttons
def click(event):
    text = event.widget.cget('text')
    if text == '=':
        expr = screenval.get()
        try:
            # Replace the "math.sin(" function    
            calc_expr = expr.replace('sin(', 'math.sin(math.radians(')
            calc_expr = calc_expr.replace('cos(', 'math.cos(math.radians(')
            calc_expr = calc_expr.replace('tan(', 'math.tan(math.radians(')
            calc_expr = calc_expr.replace('sqrt(', 'math.sqrt(math.radians(')

            sin_count = expr.count('sin(')
            cos_count = expr.count('cos(')
            tan_count = expr.count('tan(')
            sqrt_count = expr.count('sqrt(')

            calc_expr = calc_expr + ')' * (sin_count + cos_count + tan_count + sqrt_count)

            value = eval(calc_expr)
            screenval.set(value)

            # Save to history
            hist_box.insert(END, f"{expr} = {value}")
            screenval.set(value)
        except:
            screenval.set("Error")

    elif text == 'C':
        screenval.set("")
        TextArea.update()
    elif text in ['sin', 'cos', 'tan', 'sqrt']:
        # Add the function with opening parenthesis
        screenval.set(screenval.get() + f"{text}(")
        TextArea.update()
    else:
        screenval.set(screenval.get() + text)
        TextArea.update()

def dlt():
    try:
        selected = hist_box.curselection()
        hist_box.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please a value")

# Entry box to show the numbers
screenval = StringVar()
screenval.set("")
TextArea = Entry(win, font='lucida 16 bold', borderwidth=2, relief=SUNKEN, textvariable=screenval)
TextArea.pack(ipadx=220, ipady=20, pady=10)

# Frame1 to pack buttons(for basic calculation)
frame = Frame(win, bg='grey')
frame.place(x=25, y=100)

btn = Button(frame, text='1', font='lucida 13 bold')
btn.pack(ipadx=16,ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='2', font='lucida 13 bold')
btn.pack(ipadx=16, ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='3', font='lucida 13 bold')
btn.pack(ipadx=16, ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)

# Frame2 to pack buttons
frame = Frame(win, bg='grey')
frame.place(x=25, y=160)

btn = Button(frame, text='4', font='lucida 13 bold')
btn.pack(ipadx=16,ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='5', font='lucida 13 bold')
btn.pack(ipadx=16, ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='6', font='lucida 13 bold')
btn.pack(ipadx=16, ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)

# Frame3 to pack buttons
frame = Frame(win, bg='grey')
frame.place(x=25, y=220)

btn = Button(frame, text='7', font='lucida 13 bold')
btn.pack(ipadx=16,ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='8', font='lucida 13 bold')
btn.pack(ipadx=16, ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='9', font='lucida 13 bold')
btn.pack(ipadx=16, ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)

# Frame4 to pack buttons
frame = Frame(win, bg='grey')
frame.place(x=25, y=280)

btn = Button(frame, text='/', font='lucida 13 bold')
btn.pack(ipadx=17,ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='*', font='lucida 13 bold')
btn.pack(ipadx=18, ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='-', font='lucida 13 bold')
btn.pack(ipadx=18, ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)

# Frame5 to pack buttons
frame = Frame(win, bg='grey')
frame.place(x=200, y=280)

btn = Button(frame, text='0', font='lucida 13 bold')
btn.pack(ipadx=18,ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)

# Frame6 to pack buttons
frame = Frame(win, bg='grey')
frame.place(x=200, y=160)

btn = Button(frame, text='=', font='lucida 13 bold')
btn.pack(ipadx=17,ipady=40 ,side=LEFT)
btn.bind("<Button-1>", click)

# Frame6 to pack buttons
frame = Frame(win, bg='grey')
frame.place(x=200, y=100)

btn = Button(frame, text='+', font='lucida 13 bold')
btn.pack(ipadx=17,ipady=10 ,side=LEFT)
btn.bind("<Button-1>", click)

# Frame7 to pack buttons(for scientific calculation)
frame = Frame(win, bg='grey')
frame.place(x=480, y=100)

btn = Button(frame, text='tan', font='lucida 13 bold')
btn.pack(ipadx=17,ipady=10 ,side=RIGHT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='cos', font='lucida 13 bold')
btn.pack(ipadx=18, ipady=10 ,side=RIGHT)
btn.bind("<Button-1>", click)
btn = Button(frame,text='sin', font='lucida 13 bold')
btn.pack(ipadx=18, ipady=10 ,side=RIGHT)
btn.bind("<Button-1>", click)

# Frame8 to pack buttons
frame = Frame(win, bg='grey')
frame.place(x=480, y=160)

btn = Button(frame, text='%', font='lucida 13 bold')
btn.pack(ipadx=22, ipady=10, side=RIGHT)
btn.bind("<Button-1>", click)
btn = Button(frame, text='**', font='lucida 13 bold')
btn.pack(ipadx=20, ipady=10, side=RIGHT)
btn.bind("<Button-1>", click)
btn = Button(frame, text='sqrt', font='lucida 13 bold')
btn.pack(ipadx=18, ipady=10, side=RIGHT)
btn.bind("<Button-1>", click)

# Frame9 to pack button
frame = Frame(win, bg='grey')
frame.place(x=480, y=280)

btn = Button(frame, text='Delete', font='lucida 13 bold', command=dlt)
btn.pack(ipadx=82, ipady=10, side=RIGHT)

# Frame10 t pack buttons
frame = Frame(win, bg='grey')
frame.place(x=480, y=220)

btn = Button(frame, text='C', font='lucida 13 bold')
btn.pack(ipadx=25, ipady=10, side=RIGHT)
btn.bind("<Button-1>", click)

frame = Frame(win, bg='grey')
frame.place(x=560, y=220)

btn = Button(frame, text=')', font='lucida 13 bold')
btn.pack(ipadx=25, ipady=10, side=RIGHT)
btn.bind("<Button-1>", click)

frame = Frame(win, bg='grey')
frame.place(x=640, y=220)

btn = Button(frame, text='.', font='lucida 13 bold')
btn.pack(ipadx=24, ipady=10, side=RIGHT)
btn.bind("<Button-1>", click)

# Listbox for seeing the history
hist_box = Listbox(win, font='lucida 10 bold')
hist_box.pack(padx=310, pady=32, ipady=6, ipadx=25)



# Run the window
win.mainloop()