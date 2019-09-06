import tkinter
from tkinter import *
from tkinter import messagebox

m=tkinter.Tk()
str = StringVar()
def about():
    str.set("A Simple python Calculator By Mohit Misra<mhtmsr>\nNational Institute of Science and Technology")
def value(value):
    global str
    return str.set(str.get()+value)
def calculate():
    try:
        global str
        return str.set(eval(str.get()))
    except ArithmeticError:
        messagebox.showinfo("Error", "Invalid Calculation")
    except SyntaxError:
        messagebox.showinfo("Error", "Invalid Calculation")
m.title("pyCalculator v1.0")
m.iconbitmap('calcicon.ico')
# setting geometry of tk window
m.geometry("400x500")
m.configure(background="black")
m.resizable(width=False, height=False)
menubar=Menu(m)
m.config(menu=menubar)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=m.destroy)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="About", command=lambda:about())
b1=Button(m, text='1', height="3", width="5", command=lambda: value("1"))
b1.place(relx=0.09, rely=0.4)
b2=Button(m, text='2', height="3", width="5", command=lambda: value("2"))
b2.place(relx=0.25, rely=0.4)
b3=Button(m, text='3', height="3", width="5", command=lambda: value("3"))
b3.place(relx=0.41, rely=0.4)
b4=Button(m, text='4', height="3", width="5", command=lambda: value("4"))
b4.place(relx=0.09, rely=0.55)
b5=Button(m, text='5', height="3", width="5", command=lambda: value("5"))
b5.place(relx=0.25, rely=0.55)
b6=Button(m, text='6', height="3", width="5", command=lambda: value("6"))
b6.place(relx=0.41, rely=0.55)
b7=Button(m, text='7', height="3", width="5", command=lambda: value("7"))
b7.place(relx=0.09, rely=0.7)
b8=Button(m, text='8', height="3", width="5", command=lambda: value("8"))
b8.place(relx=0.25, rely=0.7)
b9=Button(m, text='9', height="3", width="5", command=lambda: value("9"))
b9.place(relx=0.41, rely=0.7)
bequal=Button(m, text='=', height="3", width="20", command=lambda: calculate())
bequal.place(relx=0.6, rely=0.88)
b0=Button(m, text='0', height="3", width="20", command=lambda: value("0"))
b0.place(relx=0.1, rely=0.86)
bplus=Button(m, text='+', height="3", width="20", command=lambda: value("+"))
bplus.place(relx=0.6, rely=0.4)
bminus=Button(m, text='-', height="3", width="20", command=lambda: value("-"))
bminus.place(relx=0.6, rely=0.52)
bdivide=Button(m, text='/', height="3", width="20", command=lambda: value("/"))
bdivide.place(relx=0.6, rely=0.64)
bmultiply=Button(m, text='*', height="3", width="20", command=lambda: value("*"))
bmultiply.place(relx=0.6, rely=0.76)
bclear=Button(m, text='Clear', height="3", width="50", command=lambda: str.set(""))
bclear.place(relx=0.05, rely=0.26)
mainbox = Label(m, textvar=str, bg="white", font="20", bd="5", height=6, width=400, relief="raised", cursor="arrow")
mainbox.place(relx=0.52, rely=0.13, anchor=CENTER)
m.mainloop()
