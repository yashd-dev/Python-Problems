from datetime import datetime
from playsound import playsound  # This is used for playing sounds
import multiprocessing  # This if for stoping the sound
import random  # This is for randomly genrating the Values


def sums(p):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(1, 2)  # To randomly decide whether to add or subtract
    global counter  # global because we dont want our values back to default every iteration
    value = 0
    if z == 1:
        try:
            value = int(input(f"Enter the Sum of {x} and {y}: "))
        except:
            pass
        ans = x+y

        if value == ans:
            if counter == 3:
                print("All Corect!")
            counter += 1
            print(f"{counter} Corect, next")
    elif z == 2:
        try:
            value = int(input(f"Enter the Diffrence of {x} and {y}: "))
        except:
            pass
        ans = x-y
        if value == ans:
            counter += 1
            if counter == 3:
                print("All Corect!")
            else:
                print(f"{counter} Corect, next")
    if counter == 3:
        print("All Sums Completed, Shutting the alarm")
        return False
    else:
        return True


counter = 0
alarm_time = input("Enter the time of alarm to be set:HH:MM AM/PM\n") # Example: 05:30 PM or 05 30 PM
alarm_hour = alarm_time[0:2]  # Slicing the hours from user input
alarm_minute = alarm_time[3:5]  # Slicing the minutes from user input
alarm_period = alarm_time[6:8].upper()  # Slicing the AM/PM from user input
print("Setting up alarm..")
while True:  # Because we want to check for the current times continuously
    now = datetime.now()
    current_hour = now.strftime("%I")  # Current Hour
    current_minute = now.strftime("%M")  # Current Minutes
    current_period = now.strftime("%p")  # Current Period ie AM/PM
    if (alarm_period == current_period):
        if (alarm_hour == current_hour):
            # Checking if curent time is matching the users given time
            if (alarm_minute == current_minute):
                print("Wake Up!")
                p = multiprocessing.Process(
                    target=playsound, args=("audio.mp3",))  # Im doing this because playsound just plays sound and doesnt stop on keyboard interuption
                p.start()
                condition = True
                while condition:
                    # Calling the sums function which asks users math question
                    condition = sums(p)
                p.terminate()
                break  # To exit the loop
