from tkinter import *
root=Tk()
root.title("DEMO WINDOW")
root.geometry("300x300")
root.configure(bg="skyblue")
demo=Label(text="hello",fg="black",bg="white",height=1,width=300)
name=Label(text="FULLNAME",bg="lavender")
name_entry=Entry()
text_box=Text(height=3)
def display():
    name1=name_entry.get()
    global Message
    Message=" welcome "
    greet="hey there "+name1
    text_box.insert(END,greet)
    text_box.insert(END,Message)
BTN=Button(text="Begin",command=display,height=1, bg="black",fg="white")
demo.pack()
name.pack()
name_entry.pack()
BTN.pack()
text_box.pack()
root.mainloop()
    
    
    
    
    