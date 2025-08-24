def cube(x):
    return x**3

def square(x):
    return x*x

num = int(input("Enter a number: "))
cube_result = cube(num)
square_result = square(num)
print(f"The square of {num} is: {square_result}")
print(f"The cube of {num} is: {cube_result}")
