print(3+4)
print(3-4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Fortune'))
print(type('Richman'))
print(type('Nigeria'))


import random
import string

no_char = int(input("Enter the number of characters: "))
no_ids = int(input("Enter number of Ids to be generated: "))

def random_user_id():
    for i in range(no_ids):
        lists = []
        for x in range(no_char):
            a = random.choice(string.hexdigits)
            lists.append(a)
        a = print(''.join(lists))
    return a
    

print(random_user_id())
