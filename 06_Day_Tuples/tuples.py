# Level 1
empty = tuple()
sisters = ('Ananya', 'Riya')
brothers = ('Rohit', 'Anay')
siblings = sisters + brothers
print(len(siblings))
family_members = siblings + ('Manish', 'Vandana')

# Level 2
*sibs, father, mother = family_members
print(sibs)
print(father)
print(mother)

fruits = ('banana', 'apple')
vegetables = ('Cabbage', 'Cauliflower')
animal_products = ('Milk', 'Leather')
food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

food_stuff_lt = food_stuff_lt[:len(food_stuff_lt) // 2] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]
food_stuff_tp = tuple(food_stuff_lt)
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[len(food_stuff_lt) - 3:]
print(food_stuff_lt)
print(first_three)
print(last_three)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
