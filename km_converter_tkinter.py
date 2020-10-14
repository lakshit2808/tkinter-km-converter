from tkinter import *

windows = Tk()

def km_converter():
    cm =float(e1_value.get())*100000
    mtr=float(e1_value.get())*1000
    mile=float(e1_value.get())*0.62
    
    d1.delete("1.0", END)
    d1.insert(END,cm)

    d2.delete("1.0" , END)
    d2.insert(END,mtr)

    d3.delete("1.0" , END)
    d3.insert(END , mile)

lbl = Label(windows,text="KM")
lbl.grid(row=0,column=0)

b1=Button(windows,text="Convert" , command=km_converter)
b1.grid(row=0,column=2)

e1_value = StringVar()
e1=Entry(windows , textvariable=e1_value)
e1.grid(row=0,column=1)

d1=Text(windows , height=1, width=15)
d1.grid(row=1 , column=0)

d2=Text(windows , height=1 , width=15)
d2.grid(row=1 , column=1)


d3=Text(windows , height=1 , width=15)
d3.grid(row=1 , column=2)

windows.mainloop()

