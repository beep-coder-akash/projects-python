from tkinter import * 

win = Tk()
win.minsize(width=300, height=200)
win.maxsize(width=300, height=200)
win.title('Temparature Converter')

# Function for C to F
def c_to_f():
    try:
        celsius = float(ent.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{fahrenheit:.2f} F")
    except ValueError:
        result_label.config(text='Enter a Valid Number')

# Function for F to C
def f_to_c():
    try:
        fahrenheit = float(ent.get())
        celsius = (fahrenheit - 32) *5/9
        result_label.config(text=f"{celsius:.2f} C")
    except ValueError:
        result_label.config(text='Enter a Valid Number')

# Entry box
ent = Entry(win, font='Arial 10 bold', borderwidth=3, relief=SUNKEN)
ent.pack(ipadx=16, pady=15, ipady=3)

# Button F to C
btn1 = Button(win, text='fahrenheit -> Celsius', command=f_to_c)
btn1.pack()
btn2 = Button(win, text='Celsius -> fahrenheit', command=c_to_f)
btn2.pack(pady=8)

# Result
result_label = Label(win, text="", font='Arial 15 bold')
result_label.pack(pady=8)

# Run the function
win.mainloop()