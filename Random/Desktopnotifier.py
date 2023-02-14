from win10toast import ToastNotifier
import time
var=ToastNotifier()
while True:
    var.show_toast(title="Stand Up Now", msg="Go drink water or something but just stand for 5 mins minimum", icon_path="heart_icon.ico", duration=30,)
    time.sleep(1800) #Repeats after every 30 mins
    


