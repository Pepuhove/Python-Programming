def main():
    size = get_size()
    symbol = get_symbol()
    print(f"\nHere is a square with {size} '{symbol}'(s):\n")
    square(size, symbol)

def get_size():
    """Ask the user for a positive integer size."""
    while True:
        try:
            size = int(input("Enter the size of the square: "))
            if size > 0:
                return size
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer (1..9).")

def get_symbol():
    """Ask the user for a symbol."""
    while True:
        symbol = input("Enter a symbol: ").strip()
        if len(symbol) == 1:  # Ensure only a single character
            return symbol
        else:
            print("Please enter a single symbol.")

def square(size, char):
    """Prints a square of the given size using the given character."""
    for _ in range(size):
        print((char + " ") * size)

main()
