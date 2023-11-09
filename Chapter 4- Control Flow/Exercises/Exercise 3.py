# Alien Colors 3

## Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
## •	 If the alien is green, print a message that the player earned 5 points.
## •	 If the alien is yellow, print a message that the player earned 10 points.
## •	 If the alien is red, print a message that the player earned 15 points.
## •	 Write three versions of this program, making sure each message is printed for the appropriate color alien.


##### Attempt
### Version 1
print("Version 1: Yellow Alien")
alien_color = 'yellow'

if alien_color=='green':
    print("You earned 5 points from shooting the alien.")
elif alien_color=='yellow':
    print("You earned 10 points from shooting the alien.")
else:
    print("You earned 15 points from shooting the alien.")

print("\n")

### Version 2
print("Version 2: Green Alien")
alien_color='green'

if alien_color=='green':
    print("You earned 5 points from shooting the alien.")
elif alien_color=='yellow':
    print("You earned 10 points from shooting the alien.")
else:
    print("You earned 15 points from shooting the alien.")


print("\n")

### Version 3
print ("Version 3: Red Alien")

alien_color='red'

if alien_color=='green':
    print("You earned 5 points from shooting the alien.")
elif alien_color=='yellow':
    print("You earned 10 points from shooting the alien.")
else:
    print("You earned 15 points from shooting the alien.")


### using list
print("\n[Personal Activity]: input with elif, list")
ask=("\nAvailable Colors: green, yellow, red")
ask+=(f"\nWhich color was the alien you shot down?: ")

alien_colors=['green', 'yellow', 'red']
    
colorinput=input(ask)

if colorinput in alien_colors[0]:
    print(">>>>\tYou have earned 5 points.")
elif colorinput in alien_colors[1]:
    print(">>>>\tYou have earned 10 points.")
elif colorinput not in alien_colors:
    exit()
else:
    print(">>>>\tYou have earned 15 points.")

exit()