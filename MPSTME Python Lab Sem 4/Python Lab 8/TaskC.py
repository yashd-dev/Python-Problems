import tkinter as tk

window = tk.Tk()
window.title("App Calculator")
window.geometry( ) 
window.config(bg="Turquoise")
dobtitle=tk.Label(window,text="Date Of Birth",font="Helvetica 20 bold",bg="red").place(x=10,y=10)

daylabel=tk.Label(window,text="Day: ",font="Helvetica 15 bold",bg="cyan").place(x=10,y=50)
monthlabel=tk.Label(window,text="Month: ",font="Helvetica 15 bold",bg="cyan").place(x=10,y=100)
yearlabel=tk.Label(window,text="Year: ",font="Helvetica 15 bold",bg="cyan").place(x=10,y=150)

dayentry=tk.Entry(window).place(x=100,y=50)
monthentry=tk.Entry(window).place(x=100,y=100)
monthentry=tk.Entry(window).place(x=100,y=150)

datetitle=tk.Label(window,text="Date Of Birth",font="Helvetica 20 bold",bg="red").place(x=350,y=10)

daylabel=tk.Label(window,text="Given Day: ",font="Helvetica 15 bold",bg="cyan").place(x=300,y=50)
monthlabel=tk.Label(window,text="Given Month: ",font="Helvetica 15 bold",bg="cyan").place(x=290,y=100)
yearlabel=tk.Label(window,text="Given Year: ",font="Helvetica 15 bold",bg="cyan").place(x=300,y=150)

dayentry=tk.Entry(window).place(x=430,y=50)
monthentry=tk.Entry(window).place(x=430,y=100)
monthentry=tk.Entry(window).place(x=430,y=150)

Result=tk.Label(window,bg="black",fg="white",font="Helvetica 15 bold",text="Resultant Age").place(x=200,y=230)
Resultentry=tk.Entry(window).place(x=200,y=270)
years=tk.Label(window,font="Helvetica 15 bold",text="Resultant Years").place(x=190,y=330)
Resultentry=tk.Entry(window).place(x=200,y=400)
Result=tk.Label(window,font="Helvetica 15 bold",text="Resultant Age").place(x=200,y=470)
Resultentry=tk.Entry(window).place(x=200,y=520)
window.mainloop()