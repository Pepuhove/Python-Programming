def main():
    num = get_int("Enter a number: ")
    print(f"The number that you entered is: {num}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) 
        except ValueError:
            pass
       
main()