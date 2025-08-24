import csv

name = input("What's your name?: ").strip()
home = input("Where is your home? ").strip()

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
