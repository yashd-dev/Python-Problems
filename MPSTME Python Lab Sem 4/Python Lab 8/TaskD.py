import tkinter as tk
import tkcalendar as tkcal

win=tk.Tk()
win.title("Calendar")
win.geometry("700x600")

calander=tkcal.Calendar(win, selectmode="day",year= 2023, month=3, day=17)
calander.pack(fill="both", expand=True,pady=50)

button=tk.Button(text="SHow").place(x=150,y=550)
button=tk.Button(text="Clear").place(x=300,y=550)
button=tk.Button(text="Exit").place(x=450,y=550)
win.mainloop()
