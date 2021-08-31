# Level 1
# 1
age = int(input('Enter age: '))
if age>= 18:
    print("You are old enough to drive.")
else:
    print("You need to wait", 18-age, "years.")

# 2
my_age = 18

if age == my_age:
    print("We are the same age")
elif age > my_age:
    print("You are", age - my_age, "years older than me")
else:
    print("I am", my_age-age, "years older than you")

# 3
a = int(input("Enter number: "))
b = int(input("Enter number: "))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is lesser than", b)
else:
    print("Both numbers are equal")
