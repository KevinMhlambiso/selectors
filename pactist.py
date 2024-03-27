from tkinter import *

Windows = Tk()
def delete():
     listbox.delete(listbox.curselection())
     listbox.config(height=listbox.size())

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def submit():
    print("place your order :")
    print(listbox.get(listbox.curselection()))

listbox = Listbox(Windows, bg="#f7ffde", font=("",35),width=12)
listbox.pack()

listbox.insert(1,"muffin")
listbox.insert(2,"cake")
listbox.insert(3,"ice cream")
listbox.insert(4,"chocolate")
listbox.insert(5,"pie")
listbox.insert(6,"puff pastry")
listbox.insert(7,"lollipop")
listbox.insert(8,"puding")
listbox.insert(9,"donuts")

listbox.config(height=listbox.size())

entryBox = Entry(Windows)
entryBox.pack()

submitButton = Button(Windows,text="submit", command=submit)
submitButton.pack()

addButton = Button(Windows,text="add", command=add)
addButton.pack()

deleteButton = Button(Windows,text="delete", command=delete)
deleteButton.pack()

Windows.mainloop()