def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10))

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
#print(is_even(7)) # False

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

total = 0
for i in range(5):
    total+=i
print(total)

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

def generate_groups (team,*args):
    
    for i in args:
        print(team)
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))


def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))


# Excercises

