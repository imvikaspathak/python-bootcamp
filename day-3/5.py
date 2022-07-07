#leap year programme
year = int(input("which year you wan to check "))

if year%4 != 0:
    print("not a leap year")
else:
    if year%100 != 0:
        print("this is leap year")
    else:
        if year%400 == 0:
            print("this year is leap year")
        else:
            print("this is not leap year")

