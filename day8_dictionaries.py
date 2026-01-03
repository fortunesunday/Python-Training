dog = {}
dog['name'] = 'Ralph'
dog['colour'] = 'White'
dog['breed'] = 'Rottweiler'
dog['age'] = 4

print(dog)

student = {}
student['first_name'] = 'Mary'
student['last_name'] = 'Ekanem'
student['gender'] = 'female'
student['age'] = 22
student['marital status'] = 'single'
student['skills'] = ['Graphic design', 'Research', 'Public speaking']
student['country'] = 'Nigeria'
student['city'] = 'Uyo'
student['address'] = 'Abak road'

print(student)
print(len(student))
print(type(student['skills']))

print(student.keys())
print(student.values())
print(student.items())

student.pop('city')
print(student)

#del dog
print(dog)