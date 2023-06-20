import tkinter
from tkinter import*

root = Tk()
root.title("login")
root.geometry("500x500")
username=Label(root,text="username",background="lightblue")
username.grid(column=2,row=1)
text = Entry(root,width=20)
text.grid(column=2,row=2)
password=Label(root,text="password",background="lightblue")
password.grid(column=2,row=3)
text2 = Entry(root,width=20)
text2.grid(column=2,row=4)
root.mainloop()