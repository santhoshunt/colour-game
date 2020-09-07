from tkinter import *
from random import *
from tkinter import messagebox
import keyboard

window=Tk()
bgc=["#E9967A",'#FA8072','#F08080','#0B5345','#FFA07A','#4A235A' ,'#515A5A' ,'#D2B4DE' ,'#979A9A','#9A7D0A']
colours=['red','blue','green','yellow','black',"orange"]
points=0
def check():
    global points,ran,label,ptlabel
    if ent.get().lower()==ran:
        points+=1
        ent.delete(0,END)
        ran=choice(colours)
        label.config(text=choice(colours),fg=ran)
        bgcolour=choice(bgc)
        ptlabel.config(text=f"Your points are : {points}",bg=bgcolour)
        window.config(bg=bgcolour)
        label.config(bg=bgcolour)
    else:
        pt=points
        points=0
        ptlabel.config(text=f"Your pointis : 0",bg=bgcolour)
    if points ==0:
        messagebox.showerror("You lost",f"It's actually \"{ran.upper()}\" but you've entered \"{ent.get().upper()}\"\nYour points : {pt}")
        ent.delete(0,END)
ran=choice(colours)
ptlabel=Label(window,text="Your point : 0")
label=Label(window,text=choice(colours),fg=ran,font=("bold",20))
ent=Entry(window,borderwidth=5,width=20)
but=Button(text="Enter",command=check)
keyboard.on_press_key('enter',lambda a:check())

ptlabel.grid()
label.grid()
ent.grid()
but.grid()

window.mainloop()