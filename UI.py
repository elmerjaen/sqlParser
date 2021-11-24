from tkinter import *
import re
import sqlParser

gui = Tk()
gui.title('SQL Syntax Analyzer')
gui.geometry('550x150')

entry_ = Entry(gui, width=60, borderwidth=2, font=('Helvetica',11,'bold'))
lbStart = Label(gui, text="A continuación, ingrese una sentencia SQL:", font=('Helvetica',12,'bold'))
myLabel = Label(gui)
img_btnVerifySql = PhotoImage(file = "./img_button.png") 

def myClick():
    global myLabel
    myLabel.destroy()
    user_input = entry_.get()
    sql_string = ''.join(re.split(' ', user_input))
    result, query_type = sqlParser.evaluate_sql(sql_string)
    if result == 1:
        myLabel = Label(gui, text=f'La sentencia {query_type} es correcta.', font=('Helvetica',12,'bold'), bg="RoyalBlue1", fg="white")
    else:
        myLabel = Label(gui, text="Sintaxis incorrecta.", font=('Helvetica',12,'bold'), bg="red", fg="white")

    myLabel.place(x=10, y=110)

def on_enter(e):
    btnVerifySql.config(bg='DarkOrange2',fg='blue')

def on_leave(e):
    btnVerifySql.config(bg='DarkOrange4',fg='white')

btnVerifySql = Button(
    gui,text="Verificar comando SQL", command=myClick, 
    font=('Helvetica',12,'bold'), fg="white",
    bg="DarkOrange4", padx=10, pady=10)

#btnVerifySql = Button(gui,image=img_btnVerifySql, borderwidth=0, command=myClick)

lbStart.pack()
entry_.pack()
btnVerifySql.place(x=150, y=50)

# btnVerifySql hover event
btnVerifySql.bind('<Enter>', on_enter)
btnVerifySql.bind('<Leave>', on_leave)

gui.mainloop()