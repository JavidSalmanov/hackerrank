def is_leap(year):
    leap = True
    # if (year % 4 != 0) or ((year % 4 == 0) and (year % 100 ==0)) or ((year % 4 == 0) and (year % 100 ==0) and (year % 400 !=0)):

    if(year % 4 == 0):
        if(year % 100 == 0):
            leap = False
        if(year % 400):
            leap = True
        return leap
    else:
        return True


year = int(input())
print(is_leap(year))

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
