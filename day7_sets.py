# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)

it_companies.update(('Meta', 'Optimus'))
print(it_companies)

it_companies.remove('Meta')
print(it_companies)

# .discard() does not raise an error if you try to remove a non existent item. .remove would raise an error.

# Exercise 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A

# Exercise 3
sa = set(age)
print(len(sa) == len(age))
print(sa)
print(age)

sentence = "I am a teacher and I love to inspire and teach people"
ls = sentence.split() # first convert to list
print(ls)
ss = set(ls) # convert to a set; it gives you distinct values with no duplicates
print(ss)
print(len(ss)) # to find number of unique words used in the sentence
