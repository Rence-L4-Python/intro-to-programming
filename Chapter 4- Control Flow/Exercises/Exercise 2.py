# Alien Colors 2

## Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
## •If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
## •If the alien’s color isn’t green, print a statement that the player just earned 10 points.
## •Write one version of this program that runs the if block and another that runs the else block.


##### Attempt
### If Block
print("if block:")
alien_color='green'

if alien_color=='green':
    print("You earned 5 points from shooting the green alien.")
else:
    print("You earned 10 points from shooting another alien.")

print("\n")
print("else block:")

alien_color='yellow'
if alien_color=='green':
    print("You earned 5 points from shooting the green alien.")
else:
    print("You earned 10 points from shooting another alien.")


### input
print("\n[Personal Activity] input:")

ask=("What is the color of the alien you shot down?: ")

alien_color='green'
colorinput=input(ask)
if colorinput == alien_color:
    print("You earned 5 points from shooting a green alien.")
else:
    print("You have earned 10 points from shooting another alien.")

exit()