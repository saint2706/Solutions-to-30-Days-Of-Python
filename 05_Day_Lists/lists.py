# Level 1

# 1
empty_list = list()

# 2
more_than_5 = [1, 2, 3, 4, 5, 6]

# 3
print(len(more_than_5))

# 4
print(more_than_5[0], more_than_5[len(more_than_5)//2], more_than_5[-1])

# 5
mixed_list = ['Rishabh', 19, 174, 'Bachelor', 'Navi Mumbai']

# 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

# 10
it_companies[0] = 'Infosys'
print(it_companies)

# 11
it_companies.append('Facebook')

# 12
it_companies = it_companies[0:len(it_companies)//2] + ['Dell'] + it_companies[len(it_companies)//2:]

# 13
it_companies = it_companies[0].upper()

# 14
it_companies_hash = '#'.join(it_companies)

# 15
print('IBM' in it_companies)

# 16
it_companies.sort()

# 17
it_companies.reverse()

# 18
it_companies = it_companies[2:]

# 19
it_companies = it_companies[:len(it_companies) - 3]

# 20
it_companies = it_companies[0:len(it_companies)//2] + it_companies[len(it_companies)//2 + 1:]

# 21
it_companies.pop(0)

# 22
it_companies.pop(len(it_companies)//2)

# 23
it_companies.pop(len(it_companies)-1)

# 24
it_companies.clear()

# 25
del it_companies

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.append(back_end)

# 27
full_stack = front_end
indx = full_stack.find('Redux')
full_stack = full_stack[:indx] + ['Python', 'SQL'] + full_stack[indx:]

# Level 2

# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])
print([ages[i] for i in range((len(ages)/2) - (1 if float(len(ages)) % 2 == 0 else 0), len(ages)/2+1)])
print(sum(ages)/len(ages))
print(ages[-1]-ages[0])
print(abs(ages[0]-sum(ages)/len(ages)))
print(abs(ages[-1]-sum(ages)/len(ages)))
