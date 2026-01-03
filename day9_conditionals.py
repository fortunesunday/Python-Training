# age = (int(input('User_input: ')))
# if age >= 18:
#     print('You are old enough to drive.')
# else:
#     print(f'You need {18-age} more years to learn to drive.')


# my_age = 20
# your_age = int(input('Enter your age: '))

# if your_age > my_age:
#     print(f'You are {your_age - my_age} years older than I am.')
# else:
#     print(f'I am {my_age - your_age} years older than you are.')


# a = int(input('Enter_first_num: '))
# b = int(input('Enter_second_num: '))
# if a>b:
#     print(f'{a} is greater than {b}.')
# else:
#     print(f'{b} is greater than {a}.')


# Exercise 2

# month = input('Enter month: ')
# if month.title() in ['December', 'January', 'February']:
#     print('The season is Winter.')
# elif month.title() in ['March', 'April', 'May']:
#     print('The season is spring.')
# elif month.title() in ['June', 'July', 'August']:
#     print('The season is Summer.')
# elif month.title() in ['September', 'October', 'November']:
#     print('The season is Autumn.')


# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input('Give me a fruit: ')
# if fruit in fruits:
#     print('That fruit already exists.')
# else:
#     fruits.append(fruit)
#     print(fruits)

# Exercise 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# print('skills' in person)
# if 'skills' in person:
#     middle = len(person['skills'])//2
#     print(person['skills'][middle])

# if 'skills' in person:
#     if 'Python' in person['skills']:
#         print('Python is one of her skills.')
#     else:
#         print('Python does not exist')


# skill_set = set(person['skills'])
# if skill_set == {'Java', 'React'}:
#     print('He is a front end developer')
# elif skill_set >= {'React', 'Node', 'MongoDB'}:
#     print('He is a fullstack developer')
# elif skill_set >= {'Node', 'Python', 'MongoDB'}:
#     print('He is a backend developer')
# else:
#     print('Unknown title.')


if person['country'] == 'Finland' and person['is_married'] == True:
    print(f"Asabeneh yetayeh lives in {person['country']}. He is married")

