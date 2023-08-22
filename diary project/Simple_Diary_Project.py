# Create a command line application where the user can write and save their thoughts for different dates
# user should be able to create and remove diaries

import datetime
import keyboard

def diary_entry():
    date = datetime.date.today()
    date = date.strftime("%d/%m/%Y")
    time = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"

    return date ,time


lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

with open("diary.txt", "a") as diary:
    diary.write(diary_entry()[0]+" "+diary_entry()[1]+"\n")
    for line in lines:
        diary.write(line + "\n")
    diary.write("\n")