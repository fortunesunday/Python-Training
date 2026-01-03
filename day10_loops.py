
# for i in range(11):
#     print(i)

# count = 0
# while count <= 10:
#     print(count)
#     count += 1

# for i in range(10, -1, -1):
#     print(i)

# count = 10
# while count >= 0:
#     print(count)
#     count -= 1

# for i in range(8):
#     print('#' * i)

# symbol = '#'
# row = 8
# col = 8
# for i in range(row):
#     for j in range(col):
#         print(symbol, end=" ")
#     print()

# for i in range(11):
#     print(f'{i} x {i} = {i*i}')

# list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# for i in list:
#     print(i)

# for i in range(0, 101, 2):
#     print(i)

# for i in range(0, 100):
#     if i % 2 == 0:
#         continue
#     print(i)

# total = 0
# for i in range(0, 101):
#     total += i
# print(total)

total = 0
for i in range(0, 101, 2):
    total += i
print(total)

for i in range(0, 100, 2):
    print(i)

total = 0
for i in range(0, 101):
    if i % 2 == 0:
        continue
    total += i
print(total)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
for fruit in fruits:
    print(fruit)