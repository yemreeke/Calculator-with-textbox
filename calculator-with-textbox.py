from tkinter import *
def calculator ():
    number1 = box.get()
    text2.config(text="Result = "+str(eval(number1)))

window = Tk()
window.title("BlueGrays")
window.geometry("200x160")

text1 = Label(window)
text1.config(text ="-------------Calculator-------------")
text1.pack()

text2= Label(window)
text2.config(text ="Result => ")
text2.pack()

box = Entry(window)
box.pack()

text1 = Label(window)
text1.config(text ="")
text1.pack()

buton = Button(window)
buton.config(text="Calculate",command=calculator)
buton.pack()

text1 = Label(window)
text1.config(text ="")
text1.pack()

text1 = Label(window)
text1.config(text ="Coded: BlueGrays")
text1.pack()

mainloop()
