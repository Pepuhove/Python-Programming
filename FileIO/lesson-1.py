# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's yur name? ").strip()

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,",line.rstrip())
    
# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,",line.rstrip())

# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
        
# for name in sorted(names):
#     print(f"hello, {name}")



import csv

name = input("What's your name?: ").strip()
home = input("Where is your home? ").strip()

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name, "home":home})
