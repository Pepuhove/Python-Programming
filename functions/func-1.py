def cube(x):
    c = x**3
    def square(x):
        s = x*x
        print(s)
    square(n)
    print(c)
n = int(input("Enter a value: "))
print("The cube of {n} is:",(cube(n)))