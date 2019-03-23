# samiro0on         # mahmoudsamir109@gmail.com             # 23/03/2019

def isLeap(year):
    leap = False
    if year%4 == 0:
        if year%100 != 0:
            leap = True
        else:
            if year%400 == 0:
                leap = True
    return leap

year = int(input("please enter a year .... "))

print("this year is a leap year ...", isLeap(year))