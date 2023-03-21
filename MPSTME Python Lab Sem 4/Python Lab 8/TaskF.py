import tkinter as tk

win=tk.Tk()
win.title("Stupid Calculator")
win.geometry("510x424")

frame1 = tk.Frame(win, highlightbackground="blue", highlightthickness=2)
frame1.pack()

lable=tk.Label(frame1,text="First Number").place(x=50,y=100)
lable=tk.Label(frame1,text="Second Number").place(x=50,y=150)

entru=tk.Entry(frame1).place(x=200,y=100)
entru=tk.Entry(frame1).place(x=200,y=150)

win.mainloop()