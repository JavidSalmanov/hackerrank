def my_gen(num):
    n = 1
    while n <= num:
        print("This is printed:", n)
        yield n
        n += 1

