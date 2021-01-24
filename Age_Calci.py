import datetime

from tkinter import *

from tkinter.ttk import Combobox


screen1= Tk()
screen1.title('Age calculator')
screen1.geometry('600x500')
c=Canvas(screen1,width=500,height=250)
c.pack(side='top')


def ba():
    pin= Person(datetime.date(int(cb2.get()),int(cb3.get()),int(cb1.get())))

    t5=Label(screen1,text="Hii you are {age} year old".format(age=pin.age()),fg='red',font=('Arial',14))
    t5.place(x=230,y=400)
           
class Person:
        def __init__(self,bdate):
            self.bdate=bdate

        def age(self):
            today=datetime.date.today()
            age=today.year-self.bdate.year
            return age    

t3=Label(screen1,text='D.O.B:-',font=('Arial',18)).place(x=174,y=262)

cb1=Combobox(screen1,width=3,font=('Arial',14))

cb1['values']=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,"Text"]
        
cb1.current(1)

cb1.place(x=260,y=265)

cb3=Combobox(screen1,width=3,font=('Arial',14))

cb3['values']=[1,2,3,4,5,6,7,8,9,10,11,12]

cb3.current(1)

cb3.place(x=315,y=265)
           
cb2=Combobox(screen1,width=5,font=('Arial',14))
cb2['values']=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

cb2.current(1)

cb2.place(x=370,y=265)

bs=Button(screen1,text="Go and Check",bg='cyan2',command=ba).place(x=270,y=315)




        
