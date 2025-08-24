def main():
    name = get_name()
    age = get_age()
    favorite = get_favorites()
    print(f"My name is {name}, I am {age} years old, I like {favorite} color.")

def get_name():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            return name
        else:
            print("Please enter letters only.")
            
def get_favorites():
    while True:
        favorite = input("What is your favorite color? ")
        if favorite.isalpha():
            return favorite
        else:
            print("Please enter your favorite.")
            
def get_age():
    while True:
        age = input("What is your age? ")
        if age.isdigit():
            return age
        else:
            print("Please enter digits only.")
    
main()