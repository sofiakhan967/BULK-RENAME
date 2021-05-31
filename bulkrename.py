import os 
from tkinter import *

def rename():
    path=r''+value.get()
    count=0
    for filename in os.listdir(path):
        os.rename(path+'\\'+filename, path+'\\'+value1.get()+str(count)+value2.get())
        count+=1


win =Tk()
win.geometry('300x400')
win.title("RENAME")

Label(win , text="Paste path of file ", font="time 20 bold" , padx=30).grid(row=0, column=2)
value=StringVar()
entryvalue=Entry(win , textvariable=value ,width=40)
entryvalue.grid(row =1 , column=2)

Label(win , text="New name ", font="time 20 bold" , padx=30).grid(row=2, column=2)
value1=StringVar()
entryvalue1=Entry(win , textvariable=value1,width=40 )
entryvalue1.grid(row =3, column=2)

Label(win , text="extension ", font="time 20 bold" , padx=30).grid(row=4, column=2)
value2=StringVar()
entryvalue2=Entry(win , textvariable=value2 ,width=40)
entryvalue2.grid(row =5, column=2)


btn = Button(win, text = 'Done', bd = '5' , command=rename ,relief=GROOVE , width=10)
btn.grid(row=6, column =2,pady=10 )
win.mainloop()
