from tkinter import *
gui=Tk()
gui.title("Gui Window")
gui.wm_iconbitmap("sizeicon.ico")
gui.configure(bg="lightgrey")


def size():
    gui.geometry(f"{wv.get()}x{hv.get()}")



gui.geometry("400x400")
hlable=Label(gui,text="Change the window size",font="Arial 12 bold",bg="lightgrey").place(x=100, y=40)
width_lable=Label(gui,text="Width",font="Arial 10 bold",bg="lightgrey").place(x=50,y=100)
height_lable=Label(gui,text="Height",font="Arial 10 bold",bg="lightgrey").place(x=50,y=160)
wv=StringVar()
hv=StringVar()
w_entry=Entry(width_lable,textvariable=wv).place(x=120,y=100,width=170)
h_entry=Entry(height_lable,textvariable=hv).place(x=120,y=160,width=170)
button=Button(gui,text="Update",command=size,font="Arial 10 bold",).place(x=70,y=220)


gui.mainloop()

