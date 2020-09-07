from tkinter import *
from random import *

window=Tk()
colours=['red','blue','green','yellow','black',"orange"]
points=0
def check():
    global points,ran,label
    if ent.get().lower()==ran:
        points+=1
        ent.delete(0,END)
        ran=choice(colours)
        label.config(text=choice(colours),fg=ran)
    else:
        points=0
    print(points)

ran=choice(colours)
label=Label(window,text=choice(colours),fg=ran,font=("bold",20))
ent=Entry(window,borderwidth=5,width=40)
but=Button(text="Enter",command=check)

label.pack()
ent.pack()
but.pack()

window.mainloop()