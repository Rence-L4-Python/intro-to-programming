# Change Guest List

## You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
## You’ll have to think of someone else to invite.
### •Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
### •Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
### •Print a second set of invitation messages, one for each person who is still in your list.


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

print('\n')

exit()