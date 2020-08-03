## ECONOMY TRACKER IN PYTHON ##
import os
import sys

## FUNCTIONS ##
if os.path.exists("expenses.txt") == False:
    fp = open("expenses.txt", "x")
    fp.close()

if os.path.exists("previousdate.txt") == False:
    fp = open("previousdate.txt", "x")
    fp.close()

def checkNewMonth():
    current = getDateNumber()
    previous = getPreviousDate()
    if current < previous:
        os.system("mv expenses.txt expenses_" + getDateMonth() + "_" + str(getYear()))
        fp = open("expenses.txt", "x")
        fp.close()

def getPreviousDate():
    fp = open("previousdate.txt", "r")
    previous = fp.read().strip()
    fp.close()
    if previous == '':
        fp = open("previousdate.txt", "w")
        fp.write(str(getDateNumber()))
        fp.close()
        preivous = getDateNumber()
    return int(previous)

def setPreviousDate(date):
    fp = open("previousdate.txt", "w")
    fp.write(str(date))
    fp.close()
    return

def getCurrent():
    fp = open("expenses.txt", "r")
    current = fp.read()
    fp.close()
    if current == '':
        fp = open("expenses.txt", "w")
        current = 0
        fp.write(str(current) + "\n")
    return float(current)

def addToCurrent(amount):
    if checkNewMonth():
        print("New month started: " + str(getDateMonth()))
    fp = open("expenses.txt", "r")
    current = fp.read()
    fp.close()
    if current == '':
        fp = open("expenses.txt", "w")
        current = float(0) + float(amount)
        fp.write(str(current) + "\n")
        fp.close()
    else:
        fp = open("expenses.txt", "w")
        current = float(current) + float(amount)
        fp.write(str(current) + "\n")
        fp.close()
    print("Previous previous date was: " + str(getPreviousDate()))
    setPreviousDate(getDateNumber())
    print("New previous date set to: " + str(getDateNumber()))
    return

def getDateNumber():
    os.system("date > out.txt")
    with open("out.txt", "r") as fp:
        date = fp.read()
    os.system("rm out.txt")
    date = date.strip()[4:6]
    date = int(date)
    return date

def getDateMonth():
    os.system("date > out.txt")
    with open("out.txt", "r") as fp:
        month = fp.read()
    os.system("rm out.txt")
    month = month.strip()[7:10]
    return month

def getYear():
    os.system("date > out.txt")
    with open("out.txt", "r") as fp:
        year = fp.read()
    os.system("rm out.txt")
    year = year.strip()[11:15]
    return int(year)

def getDate():
    return (getDateMonth() + " " + str(getDateNumber()))

## PROGRAM ##

print("Welcome to your Economy Tracker")
print("Here's a list of your options:")
print("1. Add to current month")
print("2. Check your current month")
print("3. Check last entry date")
print("t. Date Month")
print("4. Exit")
while True:
    input1 = input()
    os.system("clear")
    if (input1 == "1"):
        print("\nHow much would you like to add?")
        input2 = input()
        print("Previous amount: " + str(getCurrent()))
        addToCurrent(input2)
        print("New amount: " + str(getCurrent()))
    elif (input1 == "2"):
        print("\nYour current month expense is: " + str(getCurrent()))
    elif (input1 == "3"):
        print("\nYour last entry date was: " + str(getPreviousDate()))
        print("The current date is: " + str(getDateNumber()))
    elif (input1 == "4"):
        break
    elif (input1 == "t"):
        print(getYear())
    print("\nHere's your options again:")
    print("1. Add to current month")
    print("2. Check your current month")
    print("3. Check last entry date")
    print("t. Date Month")
    print("4. Exit")
