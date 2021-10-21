from tkinter import *
import random

root = Tk()

label = Label(root)
label2 = Label(root)
input1 = Entry(root)

root.title("Fibonacci")

root.geometry("400x400")

array = [[[1,2,3,4,5,6,7,8,9,0] ,["Head", "Tail" ] ,["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]]

def newpass():
    letter1 = str(array[0][0][random.randint(0,9)])
    letter2  = str(array[0][1][random.randint(0,1)])
    letter3 = str(array[0][2][random.randint(0, 25)])
    letter4 = str(array[0][2][random.randint(0, 25)])
    letter5 = str(array[0][2][random.randint(0, 25)])
    label2["text"] = input1.get()
    label["text"  ] = letter1 + "" + letter2 + "" + letter3 + "" + letter4 + "" + letter5

btn = Button(root,text="Generate Password", command=newpass)



label2["text"] = input1.get()

btn.place(relx = 0.5 , rely =0.7 , anchor =CENTER) 
label.place(relx = 0.5 , rely =0.6 , anchor =CENTER) 
label2.place(relx = 0.5 , rely =0.5 , anchor =CENTER)
input1.place(relx =  0.5, rely = 0.4 , anchor = CENTER)
root.mainloop()