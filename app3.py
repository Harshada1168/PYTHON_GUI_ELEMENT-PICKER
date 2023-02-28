import random
from random import *
from tkinter import *

App=Tk()
App.title("Picker")
App.geometry("250x250")
msg2=Label(App, text="Please enter element names separated by ,")
msg2.pack()
def picker():
    inp=input.get()
    lst=inp.split(',')
    picked=choice(lst)
    msg1=Label(App, text="Randomly picked element is: ")
    msg1.pack()
    msg=Label(App, text=picked)
    msg.pack()
input=Entry(App)
input.pack()
b=Button(App, text='pick', command=picker)
b.pack()
App.mainloop()