# Guest List

## If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
## Then use your list to print a message to each person, inviting them to dinner.


##### Attempt
print('\nVersion 1:\n')

guest_list=['John Singer Sargent', 'Edgar Payne', 'James Gurney']

name=guest_list[0]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development through the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list[1]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development through the years. As thanks, I would like to invite you and other great painters to dinner.")

name=guest_list[2]
print(f"\tGreetings, {name}! It has been an honor to have studied your works as they have aided in my career's development through the years. As thanks, I would like to invite you and other great painters to dinner.")

##### Shortening the code with a repeating message using 'for' loop
print('\n\n[Personal Activity]: Shortening code\n')

guest_list=['John Singer Sargent', 'Edgar Payne', 'James Gurney']
for guests in guest_list:
    print(f"\tGreetings, {guests}! It has been an honor to have studied your works as they have aided in my career's development through the years. As thanks, I would like to invite you and other great painters to dinner.")

exit()