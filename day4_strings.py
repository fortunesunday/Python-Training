a,b,c = 'boy'
print(c)

challenge = '123'
print(challenge.isdecimal())

challenge = '123'
print(challenge.isdigit())

challenge = '12.3'
print(challenge.isdecimal())

s = 'nnothelloothn'
print(s.strip('noth'))

challenge = 'thirty days of python'
print(challenge.split())

print('Thirty ' + 'Days ' + 'Of ' +'Python')

company = 'Coding For All'
print(company)
print(len(company))

print(company.upper())
print(company.lower())
print(company[0:6])
print('Coding' in company)
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
print(company.split())

string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(","))

string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split())

company = 'Coding For All'
print(company[0])
print(company[10])

company = 'Python For Everyone'
a = company.split()
acronym = ''
for i in a:
    acronym += i[0]
print(acronym)

company = 'Coding For All'
a = company.split()
acronym = ''
for i in a:
    acronym += i[0]
print(acronym)

print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
a = sentence.split()
print(a.index('because'))
#print(a.rindex('because'))
print(a[6:9])

print(company.startswith('Coding'))
print(company.endswith('Coding'))

company = '   Coding For All   '
print(company.strip())

list = ['Django', 'Flask', 'Pyramid', 'Falcon']
print("# ".join(list))

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.15 * radius ** 2
print(f'The area of a circle with the radius {radius} is {area} meters square.')




