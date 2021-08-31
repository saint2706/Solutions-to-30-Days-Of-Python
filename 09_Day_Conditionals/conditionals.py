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

# Level 2
# 1
score = int(input("Enter score: "))

grades = {}
for i in range(90, 101):
    grades[i] = 'A'
for i in range(70, 90):
    grades[i] = 'B'
for i in range(60, 70):
    grades[i] = 'C'
for i in range(50, 60):
    grades[i] = 'D'
for i in range(0, 50):
    grades[i] = 'F'

print("Grade:", grades[score])

# 2
month = input('Enter month: ').title()
if month in ["September", "October", "November"]:
    print("Autumn")
if month in ["December", "January", "February"]:
    print("Winter")
if month in ["March", "April", "May"]:
    print("Spring")
else:
    print("Summer")

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter fruit: ')
print('That fruit already exists in the list' if fruit in fruits else fruits.append(fruit))
print(fruits)