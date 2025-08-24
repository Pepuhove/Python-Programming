def main():
    size = int(input("Enter a number: "))
    print_square(size)
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("# ", end="")
        print("")
        
main()