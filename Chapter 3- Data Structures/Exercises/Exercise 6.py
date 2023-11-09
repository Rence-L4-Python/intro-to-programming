# Shrinking Guest List

## You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
### •Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
### •Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
### •Print a message to each of the two people still on your list, letting them know they’re still invited.
### •Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


##### Attempt
print('\nVersion 1:\n')

guest_list=['John Singer Sargent', 'Edgar Payne', 'James Gurney']

name=guest_list[0]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development through the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list[1]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development through the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list[2]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development through the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list[0]
print(f'\n>>>> (Unfortunately, {name} cannot come to dinner, as he has been dead for over 98 years.)\n')

## replacing guest
print('## Replaced guest:\n')

del(guest_list[0])
guest_list.insert(0, 'Nikolai Lockertsen')

name=guest_list[0]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development throughout the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list[1]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development throughout the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list[2]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development throughout the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list.pop(1)
print(f"\n>>>> (Unfortunately, we can only invite two people to dinner. Sorry, {name}!)\n")

## two people left on list
print('## Two guests left:\n')

name=guest_list[0]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development throughout the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list[1]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development throughout the years. As thanks, I would like to invite you and other great painters to dinner.")

## delete list entries
del([guest_list[0]])
del([guest_list[0]])

print('\n', guest_list)


##### Attempt on shortening code with 'for' loop
print('\n\n[Personal Activity]: Shortening code\n')

guest_list=['John Singer Sargent', 'Edgar Payne', 'James Gurney']

for guests in guest_list:
    print(f"\tGreetings, {guests}! It has been an honor to have studied your works as they have aided in my career's development throughout the years. As thanks, I would like to invite you and other great painters to dinner.")

print(f'\n>>>> (Unfortunately, {guest_list[0]} cannot come to dinner, as he has been dead for over 98 years.)\n')

## replacing guest
print('## Replaced guest:\n')

del(guest_list[0])
guest_list.insert(0, 'Nikolai Lockertsen')

for guests in guest_list:
    print(f"\tGreetings, {guests}! It has been an honor to have studied your works as they have aided in my career's development throughout the years. As thanks, I would like to invite you and other great painters to dinner.")

print(f"\n>>>> (Unfortunately, we can only invite two people to dinner. Sorry, {guest_list[1]}!)\n")
guest_list.pop(1)

for guests in guest_list:
    print(f"\tGreetings, {guests}! It has been an honor to have studied your works as they have aided in my career's development throughout the years. As thanks, I would like to invite you and other great painters to dinner.")

## delete list entries
del([guest_list[0]])
del([guest_list[0]])

print('\n', guest_list)
print('\n')

exit()
