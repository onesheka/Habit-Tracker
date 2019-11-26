from tkinter import *
import sqlite3 as sq
import datetime

window = Tk()
window.title("Habit Tracker")
window.geometry('800x600+0+0')
header = Label(window, text="HABIT TRACKER", font=("arial", 30, "bold"), fg="#740B16", bg= '#B4ECE2').pack()
window.configure(background='#F39EA7')


con = sq.connect('HT1.db')
c = con.cursor()

L1 = Label(window, text="Day Type", font=("arial", 18)).place(x=10, y=100)
L2 = Label(window, text="Day (dd)", font=("arial", 18)).place(x=10, y=150)
L3 = Label(window, text="Month (mm)", font=("arial", 18)).place(x=10, y=200)
L4 = Label(window, text="Year (yyyy)", font=("arial", 18)).place(x=10, y=250)
L5 = Label(window, text="Hours Studied", font=("arial", 18)).place(x=10, y=300)
L6 = Label(window, text="Hours Used Phone", font=("arial", 18)).place(x=10, y=350)


comp = StringVar(window)
comp.set('----')

compdb = StringVar(window)
compdb.set('----')

day = StringVar(window)
month = StringVar(window)
year = StringVar(window)
hs = StringVar(window)
hp = StringVar(window)


compound = {'Working_Day', 'Weekend', 'Holiday', 'Prior_Engagement'}

compd = OptionMenu(window, comp, *compound)  # For 1st drop down list
compd.place(x=220, y=105)

compdbase = OptionMenu(window, compdb, *compound)  # For 2nd drop down list
compdbase.place(x=100, y=500)


dayT = Entry(window, textvariable=day)
dayT.place(x=220, y=155)

monthT = Entry(window, textvariable=month)
monthT.place(x=220, y=205)

yearT = Entry(window, textvariable=year)
yearT.place(x=220, y=255)

hsT = Entry(window, textvariable=hs)
hsT.place(x=220, y=305)

hpT = Entry(window, textvariable=hp)
hpT.place(x=220, y=355)



def get():
    print("You have submitted the record")

    c.execute(
        'CREATE TABLE IF NOT EXISTS ' + comp.get() + ' (Datestamp TEXT, STUDY INTEGER, PHONE INTEGER)')

    date = datetime.date(int(year.get()), int(month.get()), int(day.get()))

    c.execute('INSERT INTO ' + comp.get() + ' (Datestamp, STUDY, PHONE) VALUES (?, ?, ?)',
              (date, hs.get(), hp.get()))
    con.commit()


    comp.set('----')
    day.set('')
    month.set('')
    year.set('')
    hs.set('')
    hp.set('')



def clear():
    comp.set('----')
    compdb.set('----')
    day.set('')
    month.set('')
    year.set('')
    hs.set('')
    hp.set('')


def record():
    c.execute('SELECT * FROM ' + compdb.get())

    frame = Frame(window)
    frame.place(x=400, y=150)

    Lb = Listbox(frame, height=8, width=25, font=("arial", 12))
    Lb.pack(side=LEFT, fill=Y)

    scroll = Scrollbar(frame, orient=VERTICAL)
    scroll.config(command=Lb.yview)
    scroll.pack(side=RIGHT, fill=Y)
    Lb.config(yscrollcommand=scroll.set)

    Lb.insert(0, 'Date, Study, Phone')

    data = c.fetchall()

    for row in data:
        Lb.insert(1, row)

    L7 = Label(window, text=compdb.get() + '      ',
               font=("arial", 16)).place(x=400, y=100)

    L8 = Label(window, text="They are ordered from most recent",
               font=("arial", 16)).place(x=400, y=350)
    con.commit()


button_1 = Button(window, text="Submit", command=get, bg='#B4ECE2', fg="#740B16", activebackground="#740B16", activeforeground="#B4ECE2", highlightcolor="white")
button_1.place(x=100, y=400)

button_2 = Button(window, text="Clear", command=clear, bg='#B4ECE2', fg="#740B16", activebackground="#740B16", activeforeground="#B4ECE2", highlightcolor="white")
button_2.place(x=10, y=400)

button_3 = Button(window, text="Open DB", command=record, bg='#B4ECE2', fg="#740B16", activebackground="#740B16", activeforeground="#B4ECE2", highlightcolor="white")
button_3.place(x=10, y=500)

window.mainloop()
