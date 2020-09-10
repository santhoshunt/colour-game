from tkinter import *
from random import *
from tkinter import messagebox
import keyboard

window=Tk()
window.geometry("500x300")
window.resizable(height=False,width=False)
window.title("Game")
bgc=["#E9967A",'#FA8072','#F08080','#0B5345','#FFA07A','#4A235A' ,'#515A5A' ,'#D2B4DE' ,'#979A9A','#9A7D0A']
rand=choice(bgc)
window.config(bg=rand)
colours=['red','blue','green','yellow','black',"orange"]
points=0
ran=choice(colours)
def check():
    global points,ran,label,ptlabel,lab
    bgcolour=choice(bgc)
    if ent.get().lower()==ran:
        points+=1
        ent.delete(0,END)
        ran=choice(colours)
        label.config(text=choice(colours),fg=ran)
        ptlabel.config(text=f"Your points: {points}",bg=bgcolour)
        window.config(bg=bgcolour)
        label.config(bg=bgcolour)
        lab.config(bg=bgcolour)
    else:
        pt=points
        points=0
        ptlabel.config(text=f"Your point : 0")
        messagebox.showerror("You lost",f"It's actually \"{ran.upper()}\" but you've entered \"{ent.get().upper()}\"\nYour points : {pt}")
        ent.delete(0,END)
    
ptlabel=Label(window,text="Your point : 0",font=("bold",20))
label=Label(window,text=choice(colours),fg=ran,font=("bold",20))
ent=Entry(window,borderwidth=5,width=20)
but=Button(text="Enter",command=check)
keyboard.on_press_key('enter',lambda a:check())
lab=Label(window,text="Enter the colour of the 'TEXT'")
ptlabel.config(bg=rand)
label.config(bg=rand)
lab.config(bg=rand)
ptlabel.grid(row=0,column=0,padx=10,pady=10)
label.grid(row=1,column=1,padx=10,pady=10)
ent.grid(row=2,column=1,padx=10,pady=10)
but.grid(row=3,column=1,padx=10,pady=10)
lab.grid(row=4,column=1,padx=10,pady=10)

window.mainloop()