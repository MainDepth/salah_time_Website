# Create a command line application where the user can write and save their thoughts for different dates
# user should be able to create and remove diaries

import datetime

def diary_entry(entry):
    date = datetime.date.today()
    date = date.strftime("%d/%m/%Y")
    return date , entry


entry = input("entry")
a = diary_entry(entry)

filepath= "diary.txt"
with open(filepath, 'a') as diary:
    diary.write("\n"+a[0]+"\n"+a[1]+"\n")
