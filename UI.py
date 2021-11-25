from tkinter import *
import re
import sqlParser

gui = Tk()
gui.title('Analizador Sintáctico SQL')
gui.geometry('550x190')

entry_ = Entry(gui, width=60, borderwidth=2, font=('Consolas',11,'bold'))
lbStart = Label(gui, text="A continuación, ingrese un comando SQL:", font=('Helvetica',11,'bold'))
myLabel = Label(gui)

def myClick():
    global myLabel
    myLabel.destroy()
    sql_string = entry_.get()
    #sql_string = ''.join(re.split(' ', user_input))
    result, query_type = sqlParser.evaluate_sql(sql_string)
    if result == 1:
        myLabel = Label(gui, text=f'La sentencia {query_type} es correcta.', font=('Helvetica',12,'bold'), bg="RoyalBlue1", fg="white")
    else:
        myLabel = Label(gui, text="Sintaxis incorrecta.", font=('Helvetica',12,'bold'), bg="red", fg="white")

    myLabel.place(x=30, y=140)

def on_enter(e):
    btnVerifySql.config(bg='LightBlue', fg='black')

def on_leave(e):
    btnVerifySql.config(bg='DarkOrange4', fg='white')

btnVerifySql = Button(
    gui,text="Verificar Comando SQL", command=myClick, 
    font=('Helvetica',12,'bold'), fg="white",
    bg="DarkOrange4", padx=10, pady=8)

# btnVerifySql hover event
btnVerifySql.bind('<Enter>', on_enter)
btnVerifySql.bind('<Leave>', on_leave)

lbStart.place(x=30, y=5)
entry_.place(x=30, y=35)
btnVerifySql.place(x=150, y=75)

gui.configure(bg='linen')
gui.mainloop()