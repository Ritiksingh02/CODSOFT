from tkinter import  *
from tkinter import font

def newtask():
  task = task_entry.get()
  if task != "":
    lb.insert(END,task)
    task_entry.delete(0,"end")
  else :
    messagebox.showwarning("warning","Please enter some task.")
def deletetask():
  lb.delete(ANCHOR)

def deletall():
  lb.delete(0,"end")
  
  

def markdone():
  task_index = lb.curselection()
  if task_index :
    lb.itemconfig(task_index,fg = "#52D017")
    
    
root = Tk()
root.title("To-Do-List")
root.geometry("300x400")
root.resizable(False,False)
root.config(bg="#fffdd0")

todo_icon = PhotoImage(file="todoicon.png")
root.iconphoto(False,todo_icon)
frame = Frame(root,width=300, height=20, bg="#fffdd0",bd=0)
frame.place(x=30, y=8)
image1 = PhotoImage(file="dock.png")
Label(root,image=image1,bg="#fffdd0",fg="#000000").place(x=5,y=8)

Label(frame, text="Enter your task.",font="Georgia 15 bold",bg="#fffdd0",fg="#F62217").pack(anchor="center")
#entry
task = StringVar()
f1 = Frame(root,width=300, height=45, bg="#fffdd0",bd=0)
f1.place(x=3, y=35)
task_entry = Entry(f1, width=15, font= "Georgia 20",bd=0)
task_entry.place(x=1,y=2)
#add button
add = PhotoImage(file="addbutton.png")
button = Button(f1,image = add,bg="#fffdd0",fg="#fff",bd=0,command=newtask)
button.place(x=260,y=1)

#list box
f2 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
f2.pack(pady=(75,0))

lb = Listbox(f2,font=('Georgia',12),width=28,height=13,bg="#32405b",fg="#F70D1A",selectbackground="#5a95ff")
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(f2)
sb.pack(side = RIGHT ,fill=BOTH)
lb.config(yscrollcommand = sb.set)
sb.config(command = lb.yview)

f3 = Frame(root,width=200,bg="#D3D3D3")
f3.place(x=20,y=350)
b1 = Button(f3, text="Delete",font="Georgia 12 bold",fg="white",bg="#F70D1A",bd=0,command=deletetask)
b1.pack(fill=BOTH, expand=True,side=LEFT)
b2 = Button(f3, text="All Clear",font="Georgia 12 bold",fg="white",bg="#F70D1A",bd=0,command=deletall)
b2.pack(fill=BOTH, expand=True,side=LEFT)
b3 = Button(f3, text="Done",font="Georgia 12 bold",fg="white",bg="#12AD2B",bd=0,command=markdone)
b3.pack(fill=BOTH, expand=True,side=LEFT)

root.mainloop()