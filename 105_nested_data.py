
student1 = {'name': 'Morty',
            'stream': 'universal quest',
            'grade': 12,
            }

student2 = {'name': 'Summer',
            'stream': 'terrestrial quest',
            'grade': 20,
            }

# list of dictionaries
students_list = [student1, student2]

print (students_list[1])

# Dictionary of dictionaries
student_dict = {
                'student1': student1,
                'student2': student2
                }

# Use the list to print individual student names
for i in students_list:
    print (i['name'])

print(students_list[0]['name'])
print(student2['name'])

# Use the dictionary to print student names
print(student_dict['student1']['name'])
print(student_dict['student2']['name'])
