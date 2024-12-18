from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))

image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text="Hey User! Welcome to Denomination Counter Application.", bg='pink')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert","Do you want to calculate the denomination count?")

    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text = "Lets get started  ˚˖𓍢.🎀༘⋆", command = msg,bg = "#007FFF", fg = "purple")
button1.place(x=260,y=360)

def topwin():

    top = Toplevel()
    top.title("Denominations Calculator")

    top.configure(bg='lavender')
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg='lavender')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='lavender')

    l1 = Label(top, text="1000", bg = 'lavender')
    l2 = Label(top, text="500", bg = 'lavender')
    l3 = Label(top, text="100", bg = 'lavender')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())

            note1000 = amount//1000
            amount = amount%1000

            note500 = amount//500
            amount = amount%500

            note100 = amount//100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note1000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    btn = Button(top,text = "Calculate", command = calculator,bg = "#007FFF", fg="white")
	#
    label.place(x=230, y=50 )
    entry.place(x=200, y=80 )
    btn.place(x=240, y=120 )
    lbl.place(x=140, y=170 )

    l1.place(x=180, y=200 )
    l2.place(x=180, y=230 )
    l3.place(x=180, y=260 )

    t1.place(x=270, y=200 )
    t2.place(x=270, y=230 )
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()
    