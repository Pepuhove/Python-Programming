# 

# i =1
# total = 0
# while i <= 10 :
#     total += i
#     i += 1
# print(f"Sum of these numbers is: {total}")

n = int(input("Enter any number: "))
count = 0

while (n>0):
    count+=1
    n = n//10
    
print(f"Count of digits: {count}")