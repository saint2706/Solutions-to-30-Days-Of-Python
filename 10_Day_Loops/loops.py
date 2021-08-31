import sys
sys.path.append('data')
import countries
import countries_data
# Level 1
# 1
for i in range(0, 11):
    print(i)

k = 0
while k <=10:
    print(k)
    k+=1

# 2
for i in range(10, -1, -1):
    print(i)

k = 10
while k >=0:
    print(k)
    k-=1

# 3
hash_string = '#'
for i in range(1, 8):
    print(hash_string*i)

# 4
for i in range(1, 9):
    for j in range(1, 9):
        print("#", end=' ')
    print()

# 5
for i in range(0, 11):
    print(i, "x", i, "=", i*i)

# 6
for lang in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(lang)

# 7
for i in range(0, 101):
    if i%2 == 0:
        print(i)

# 8
for i in range(0, 101):
    if i%2 != 0:
        print(i)

# Level 2
# 1
sum = 0
for i in range(0, 101):
    sum+=i
print("The sum of all numbers is", sum)

# 2
even_sum = 0
odd_sum = 0
for i in range(0, 101):
    if i%2 == 0:
        even_sum+= i
    else:
        odd_sum+=i
print("The sum of all even numbers is", even_sum)
print("The sum of all odd numbers is", odd_sum)

# Level 3
# 1
list_c = countries.countries
for country in list_c:
    if "land" in country:
        print(country)

# 2
fruity_list = ['banana', 'orange', 'mango', 'lemon']
rev = []
for i in range(3, -1, -1):
    rev.append(fruity_list[i])
print(rev)

# 3
list_data = countries_data.data
total_langs = []
for i in list_data:
    total_langs.append(i["languages"])
print("Languages = ", len(list(set(total_langs))))