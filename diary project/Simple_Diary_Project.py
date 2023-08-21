# Create a command line application where the user can write and save their thoughts for different dates
# user should be able to create and remove diaries

import datetime
import keyboard

def diary_entry(entry):
    date = datetime.date.today()
    date = date.strftime("%d/%m/%Y")
    time = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"

    return date ,time, entry


entry = input("entry")
a = diary_entry(entry)




filepath= "diary.txt"
if keyboard.is_pressed('esc'):
    with open(filepath, 'a') as diary:
        diary.write("\n"+a[0]+ " " + a[1]+"\n"+a[2])


