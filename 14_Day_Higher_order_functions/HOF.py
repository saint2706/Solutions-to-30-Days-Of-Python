from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Level 1
'''If you already have a list of values and you want to do the exact same operation on each of the elements in the array and return the same amount of items in the list, in these type of situations it is better to use the map method.'''
'''If you already have list of values but you only want to have items in the array that match certain criteria, in these type of situations it is better to use the filter method.'''
'''If you already have list of values, but you want to use the values in that list to create something completely new, in these type of situations it is better to use the reduce method'''

'''A higher order function is a function that takes a function as an argument OR* returns a function.'''
'''A decorator in Python is (typically) an example of a higher-order function, but there are decorators that aren't (class decorators**, and decorators that aren't functions), and there are higher-order functions that aren't decorators, for example those that take two required arguments that are functions.'''
'''A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.'''

def cube(num):
    return num ** 3
def vowel_name(name):
    if name[0] in 'aeiouAEIOU':
        return True
def sum_of_cubes(num1, num2):
    return num1 + num2
print(list(filter(vowel_name, names)))
print(list(map(cube, numbers)))
print(reduce(sum_of_cubes, list(map(cube, numbers))))