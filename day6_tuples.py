tpl = ()
sisters = ('Favour', 'Victory')
brothers = ('John', 'Michael')
siblings = sisters + brothers
print(len(siblings))

family_members = siblings + ('Mum', 'Dad')
print(family_members)

# Excercise 2
parents, siblings = family_members[-2:], family_members[0:4] 
print(parents)
print(siblings)

fruits = ('banana', 'orange')
vegetables  = ('cabbage', 'brocolli')
animal_products = ('beef', 'egg')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lst = list(food_stuff_tp)
print(food_stuff_lst)

print(food_stuff_lst[2:4])
print(food_stuff_lst[0:3])
del food_stuff_tp
print('banana' in food_stuff_lst)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)