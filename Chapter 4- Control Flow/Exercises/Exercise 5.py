# Favorite Fruit

## Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
## •Make a list of your three favorite fruits and call it favorite_fruits.
## •Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement,such as You really like bananas!


##### Attempt
### Favorite Fruits
print('\n')
print("Favorite Fruits:")
favorite_fruits=['mangoes', 'bananas', 'apples']

if 'mangoes' in favorite_fruits:
    print("Mangoes are my favorite!")
if 'apples' in favorite_fruits:
    print("Apples are my favorite!")
if 'cherries' in favorite_fruits:
    print("Cherries are my favorite!")
if 'watermelons' in favorite_fruits:
    print("Watermelons are my favorite!")
if 'coconuts' in favorite_fruits:
    print("Coconuts are my favorite!")



print("\n\n")
### using list to shorten code

## Case-sensitive! Please copy the fruits over as-is.
print("\n[Personal Activity]: Shortening code")
favorite_fruits=['Mangoes', 'Bananas', 'Apples']
ask="\nCan you guess one of my favorite fruits?: "

answer=input(ask)
if answer in favorite_fruits:
    print(f"{answer} are one of my favorite fruits!")
else:
    print("I don't like those.")

exit()