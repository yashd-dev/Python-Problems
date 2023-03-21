import tkinter.messagebox
import tkinter as tk

win=tk.Tk()
win.title("Python Lab")
win.geometry('580x640')



canvas=tk.Canvas(win,width=1920,height=1080)
oval=canvas.create_oval(50,50,400,400,fill='blue')
eye1=canvas.create_oval(140,140,170,170,fill='black')
eye2=canvas.create_oval(300,140,330,170,fill='black')
mouth=canvas.create_oval(140,350,330,250,fill='black')

# square=canvas.create_rectangle(50,50,400,400,fill='blue')
# eye1=canvas.create_rectangle(140,140,170,170,fill='orange')
# eye2=canvas.create_rectangle(300,140,330,170,fill='purple')
# mouth=canvas.create_rectangle(140,350,330,250,fill='red')

canvas.pack()
# label=tk.Label(win,text="This is a cable")
# name=tk.Entry(win,bd=5,bg="red")
# name.place(x=250,y=100)
# name.pack()
# label.place(x=100,y=100)

win.mainloop()
