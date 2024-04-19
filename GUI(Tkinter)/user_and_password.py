import tkinter
def main():
    window = tkinter.Tk()
    window.geometry("300x300")
    #window.config(bg = "cyan")
    l1 = tkinter.Label(window,text="Banking System", bg="pink",fg="blue",font=("Arial",14))
    l1.place(x=100,y=50)
    l2 = tkinter.Label(window,text="UserName", font=("aril",14))
    l3 = tkinter.Label(window,text="Password", font=("aril",14))
    l2.place(x=50,y=100)
    l3.place(x=50,y=150)
    e1=tkinter.Entry(window,width=10,font=("Arial",14))
    e2=tkinter.Entry(window,width=10,font=("Arial",14),show="*")
    e1.place(x=150,y=100)
    e2.place(x=150,y=150)
    b1=tkinter.Button(window,text="signin",fg="blue",font=("Arial",14))
    b1.place(x=120,y=200)
    
main()
