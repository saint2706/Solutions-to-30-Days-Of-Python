# 📘 Day 2

- [📘 Day 2](#-day-2)
  - [Built in functions](#built-in-functions)
  - [Variables](#variables)
  - [💻 Exercises - Day 2](#-exercises---day-2)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)

## Built in functions

In Python we have lots of built-in functions. Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, and _dir()_. In the following table you will see an exhaustive list of Python built-in functions taken from [python documentation](https://docs.python.org/3.9/library/functions.html).

![Built-in Functions](../images/builtin-functions.png)

Let us open the Python shell and start using some of the most common built-in functions.

![Built-in functions](../images/builtin-functions_practice.png)

Let us practice more by using different built-in functions

![Help and Dir Built in Functions](../images/help_and_dir_builtin.png)

As you can see from the terminal above, Python has got reserved words. We do not use reserved words to declare variables or functions. We will cover variables in the next section.

I believe, by now you are familiar with built-in functions. Let us do one more practice of built-in functions and we will move on to the next section.

![Min Max Sum](../images/builtin-functional-final.png)

## Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored.
Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Variable Name Rules

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

## 💻 Exercises - Day 2

### Exercises: Level 1

1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line

### Exercises: Level 2

1. Check the data type of all your variables using type() built-in function
1. Using the _len()_ built-in function, find the length of your first name
1. Compare the length of your first name and your last name
1. Declare 5 as num_one and 4 as num_two
   1. Add num_one and num_two and assign the value to a variable total
   2. Subtract num_two from num_one and assign the value to a variable diff
   3. Multiply num_two and num_one and assign the value to a variable product
   4. Divide num_one by num_two and assign the value to a variable division
   5. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
   6. Calculate num_one to the power of num_two and assign the value to a variable exp
   7. Find floor division of num_one by num_two and assign the value to a variable floor_division
1. The radius of a circle is 30 meters.
   1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
   2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
   3. Take radius as user input and calculate the area.
1. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
1. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

[<< Day 1](../README.md#-exercises---day-1) | [Day 3 >>](../03_Day_Operators/03_operators.md)
