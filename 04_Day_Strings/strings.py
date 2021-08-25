# 1
print('Thirty' + ' Days' + ' Of' + ' Python')

# 2
print(' '.join(['Coding', 'For', 'All']))

# 3
company = 'Coding For All'

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[7:])

# 10
print(company[company.index('Coding'):8])
print(company[company.find('Coding'):8])

# 11
print(company.replace('Coding ', 'Not '))

# 12
print('Python For Everyone'.replace('Everyone', 'All'))

# 13
print(company.split())

# 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# 15
print(company[0])

# 16
print(len(company) - 1)

# 17
print(company[10])

# 18
words = "Python For Everyone".split()
print(words[0][0] + words[1][0] + words[2][0])

# 19
words = 'Coding For All'.split()
print(words[0][0] + words[1][0] + words[2][0])

# 20
print("Coding For All".index('C'))

# 21
print("Coding For All".index('F'))

# 22
print("Coding For All People".rfind('l'))

# 23
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# 24
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

# 25
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))

# 26
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# 27
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))

# 28
print('Coding For All'.startswith('Coding'))

# 29
print('Coding For All'.endswith('coding'))

# 30
print('   Coding For All      '.rstrip().lstrip())

# 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32
print('-'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
print('Name\tAge\tCountry\tCity\nRishabh\t250\tFinland\tHelsinki')

# 35
print('radius =', 10)
print('area =', 3.14, '* radius **', 2)
print('The area of a circle with radius', 10, 'is', 314, 'meters square.')

# 36
print('8 + 6 = 14')
print('8 - 6 = 2')
print('8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')
