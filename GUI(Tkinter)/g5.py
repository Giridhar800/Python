import tkinter
import mysql.connector as m
from tkinter import messagebox
cn=m.connect(database="giridhar",user="root",password="giri")
def main():
    window=tkinter.Tk()
    window.geometry("300x300")
    l1=tkinter.Label(window,text="username",font=("Arial",14))
    l2=tkinter.Label(window,text="possword",font=("Arial",14))
    l1.place(x=50,y=100)
    l2.place(x=50,y=150)
    e1=tkinter.Entry(window,width=10,font=("Arial",14))
    e2=tkinter.Entry(window,width=10,font=("Arial",14))
    e1.place(x=150,y=100)
    e2.place(x=150,y=150)
    def app():
        w=tkinter.Tk()
        w.geometry("300x300")
    def signin():
        c=cn.cursor()
        cmd="select * from user_register where uname=%s and pwd=%s"
        c.execute(cmd,params=(e1.get(),e2.get()))
        row=c.fetchone()
        if row==None:
            messagebox.showinfo(message="invallid username or password")
        else:
            app()
    b1=tkinter.Button(window,text="signin",fg="blue",font=("arial",14),command=signin)
    b1.place(x=120,y=200)
main()
    
