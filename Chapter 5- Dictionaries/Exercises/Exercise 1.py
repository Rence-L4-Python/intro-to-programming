# Person
## Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. 
## You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.


##### Attempt
print('[Dictionary]\n')
personalinfo={
    'first_name':'Mateusz',
    'last_name':'Urbanowicz',
    'age':'37',
    'city':'Kobe',
}

print(personalinfo['first_name'])
print(personalinfo['last_name'])
print(personalinfo['age'])
print(personalinfo['city'])


##### Shortening Code attempt
print('\n\n[Personal Activity]: Shortening code\n')
print('[Dictionary]\n')
personalinfo={
    'first_name':'Mateusz',
    'last_name':'Urbanowicz',
    'age':'37',
    'city':'Kobe',
}

for info, info2 in personalinfo.items():
    print(info2)