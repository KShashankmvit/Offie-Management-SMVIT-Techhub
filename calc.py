import tkinter
from tkinter import *
# Creating window
window=tkinter.Tk()
window.title("calculator")
e=Entry(window,width=35,borderwidth=5)
e.grid(column=0,row=0,columnspan=4,padx=10,pady=10)

# global variables
fnum=''
operator=''
# Defining all functions used
def click(number):
    num=e.get()  \* Used to retrive number inserted in Entry box *\ 
    e.delete(0,END)
    e.insert(0,str(num)+str(number))

def add():      \* Used to perform addition *\ 
   global fnum
   fnum=int(e.get())
   global operator
   operator="+"
   e.delete(0,END)

def subt():      \* Used to perform subtraction *\ 
   global fnum
   fnum=int(e.get())
   global operator
   operator="-"
   e.delete(0,END)

def multi():       \* Used to perform multiplication *\ 
   global fnum
   fnum=int(e.get())
   global operator
   operator="*"
   e.delete(0,END)

def divi():         \* Used to perform division *\         
   global fnum
   fnum=int(e.get())
   global operator
   operator="/"
   e.delete(0,END)

def equal():         \* Used to compute *\ 
    s_num=e.get()
    e.delete(0,END)
    if operator=="+":
        e.insert(0,fnum+int(s_num))
    elif operator=="-":
        e.insert(0,fnum-int(s_num))
    elif operator=="*":
        e.insert(0,fnum*int(s_num))
    elif operator=="/":
        e.insert(0,fnum/int(s_num)) 

def clear():
    e.delete(0,END)

# All the Buttons used
btn_0=Button(window,text="0",padx=40,pady=20,command=lambda:click("0"))
btn_1=Button(window,text="1",padx=40,pady=20,command=lambda:click("1"))
btn_2=Button(window,text="2",padx=40,pady=20,command=lambda:click("2"))
btn_3=Button(window,text="3",padx=40,pady=20,command=lambda:click("3"))
btn_4=Button(window,text="4",padx=40,pady=20,command=lambda:click("4"))
btn_5=Button(window,text="5",padx=40,pady=20,command=lambda:click("5"))
btn_6=Button(window,text="6",padx=40,pady=20,command=lambda:click("6"))
btn_7=Button(window,text="7",padx=40,pady=20,command=lambda:click("7"))
btn_8=Button(window,text="8",padx=40,pady=20,command=lambda:click("8"))
btn_9=Button(window,text="9",padx=40,pady=20,command=lambda:click("9"))
btn_clr=Button(window,text="CLEAR",padx=80,pady=20,command=clear)
btn_add=Button(window,text="+",padx=40,pady=20,command=add)
btn_subt=Button(window,text="-",padx=40,pady=20,command=subt)
btn_multi=Button(window,text="X",padx=40,pady=20,command=multi)
btn_divi=Button(window,text="/",padx=40,pady=20,command=divi)
btn_equal=Button(window,text="=",padx=100,pady=20,command=equal)

# Position of buttons
btn_0.grid(column=0,row=4)
btn_1.grid(column=0,row=3)
btn_2.grid(column=1,row=3)
btn_3.grid(column=2,row=3)
btn_4.grid(column=0,row=2)
btn_5.grid(column=1,row=2)
btn_6.grid(column=2,row=2)
btn_7.grid(column=0,row=1)
btn_8.grid(column=1,row=1)
btn_9.grid(column=2,row=1)
btn_clr.grid(column=1,row=4,columnspan=2)
btn_add.grid(column=3,row=1)
btn_subt.grid(column=3,row=2)
btn_multi.grid(column=3,row=3)
btn_divi.grid(column=3,row=4)
btn_equal.grid(column=1,row=5,columnspan=2)

window.mainloop()
