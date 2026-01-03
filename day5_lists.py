list = []
list = ['book', 'pen', 'eraser', 'crayon', 'pencil']
print(len(list))

print(list[::2])

mixed_data_types = ['Fortune', 100, 5, 'single', 'Uyo']
it_companies =  ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)
print(len(it_companies))
print(it_companies[::3])

it_companies.append('Twitter')
print(it_companies)

it_companies.insert(4, 'Temu')
print(it_companies)

#it_companies[0] = 'FACEBOOK'
#print(it_companies)

print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)

#it_companies = "#; ".join(it_companies)
#print(it_companies)

print('IBM' in it_companies)

#it_companies.sort()
#print(it_companies)

#it_companies.sort(reverse = True)
#print(it_companies)

c = it_companies[0:3]
print(c)

d = it_companies[-3:]
print(d)

e = it_companies[4]
print(e)

# it_companies.pop(0)
# print(it_companies)

# it_companies.pop(4)
# print(it_companies)

# it_companies.pop(-1)
# print(it_companies)

it_companies.clear()
print(it_companies)

# del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

copy_full_stack = full_stack.copy()
print(copy_full_stack)


# Exercise Two

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

min = min(ages)
print(min)

max = max(ages)
print(max)

ages.append(min)
ages.append(max)

print(ages)

average_age = sum(ages)/len(ages)
print(average_age)

range = max - min

abs_min = abs(min - average_age)
abs_max = abs(max-average_age)

print(abs_min)
print(abs_max)

# Finding the median
print(len(ages)) # To be continued.

# Country Exercise
country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
a, b, c, *scandic = country_list
print(a)
print(b)
print(c)
print(scandic)

#To be continued