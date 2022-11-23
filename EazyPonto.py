from tkinter import *
import tkinter 

 
# creating main tkinter window/toplevel
master = Tk()
master.configure(bg = "#900C3F")
 
# this will create a label widget
l1 = Label(master, text = "EasyPonto", fg = "#FF5733", bg = "#900C3F")
l2 = Label(master, text = "Usuário:", fg = "white", bg = "#900C3F")
l3 = Label(master, text = "Senha:", fg = "white", bg = "#900C3F")
 
# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 1, sticky = N, rowspan= 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
l3.grid(row = 2, column = 0, sticky = W, pady = 2)
 
# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)
 
# this will arrange entry widgets
e1.grid(row = 1, column = 1, pady = 2)
e2.grid(row = 2, column = 1, pady = 2)
 
 
# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"F:\PROGRAMAÇÃO\Python\EazyPonto\Fotos dos usuários\placeholder.png")
img1 = img.subsample(2, 2)
 
# setting image with the help of label
Label(master, image = img1).grid(row = 1, column = 2,
       columnspan = 2, rowspan = 2, padx = 5, pady = 5)
 
# button widget
b1 = Button(master, text = "Logar")
b2 = Button(master, text = "Marcar")
 
# arranging button widgets
b1.grid(row = 3, column = 0, sticky = S, columnspan=2)
b2.grid(row = 3, column = 2, sticky = S, columnspan=2)
 
# infinite loop which can be terminated
# by keyboard or mouse interrupt
mainloop()