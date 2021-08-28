dog = dict()
dog = {'name': 'Bruno', 'color': 'Black', 'breed': 'pug', 'legs': 4, 'age': 4}
student_dictionary = {'first_name': 'Rishabh', 'last_name': 'Agrawal', 'gender': 'M', 'age': 19,
                      'marital_status': 'unmarried', 'skills': ['procrastinating'], 'country': 'India',
                      'city': 'Mumbai', 'address': 'lol'}
print(len(student_dictionary))
print(student_dictionary['skills'])
print(type(student_dictionary['skills']))
student_dictionary['skills'].append('Sleeping')
list_keys = list(student_dictionary.keys())
list_values = list(student_dictionary.values())
list_of_tuples = [(k, v) for k, v in student_dictionary.items()]
student_dictionary.pop('marital_status')
del dog
