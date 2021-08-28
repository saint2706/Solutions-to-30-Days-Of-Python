# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Infosys', 'Flipkart'])
it_companies.remove('Infosys')
'''remove() raises an exception/error if element is not present in set'''

# Level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B
del it_companies

# Level 3
print(len(set(age)) < len(age))  # len of list is bigger

'''
List is a non-homogeneous data structure which stores the elements in single row and multiple rows and columns
Tuple is also a non-homogeneous data structure which stores single row and multiple rows and columns
Set data structure is also non-homogeneous data structure but stores in single row
'''

string = 'I am a teacher and I love to inspire and teach people.'
print(len(set(string.split())))
