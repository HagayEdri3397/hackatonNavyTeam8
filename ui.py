from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.title("Bag of Words Meets Bags of Popcorn")
window.geometry('1100x600')
#Tittel
lbl = Label(window, text="Bag of Words Meets Bags of Popcorn",font=("Arial Bold", 40))
lbl.grid(row=0)
#space
sp = Label(window, text="     ",font=("Arial Bold", 20))
sp.grid(row=3)
lbl2 = Label(window, text="Enter text to analyze:",font=("Arial Bold", 20))
lbl2.grid(row=4)
#space

spp = Label(window, text="     ",font=("Arial Bold", 20))
spp.grid(row=5)

#to get the text txt.get()
txt = Entry(window,width=50)
txt.grid(row=7)


def clicked():
#S	lbClick.configure(text=txt.get())
	if txt.get() == '1':
		lbClick.configure(text="aaa")
	else:
		lbClick.configure(text="bbb")


def clickedR():
	lbClick.configure(text=""                    "")


		


#btn = Button(window, text="Click Me", command=clicked)
#column=0, 
btn = Button(window, text="Analyze", command=clicked)
btn.grid(row=8)
btnR = Button(window, text="Reset", command=clickedR)
btnR.grid(row=9)

lbClick = Label(window, text="                    ",font=("Arial Bold", 40))
lbClick.grid( row=10)





window.mainloop()