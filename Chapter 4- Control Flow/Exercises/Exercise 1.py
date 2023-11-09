# Alien Colors 1

## Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
## •Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
## •Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)


##### Attempt
### Test passed
print("[Version 1] Test Passed:")
alien_color='green'

if alien_color=='green':
    print("You have earned 5 points.")

print("\n")
print("[Version 2] Test Failed:")
### Test failed
alien_color='yellow'

if alien_color=='green':
    print("You have earned 5 points.")


#### input test:
print("\n")
print("[Personal Activity] input:")

question=("(Available Colors: green, yellow, red)\n")
question+=(f"\nWhich color was the alien you shot down?: ")

alien_color='green'
colorinput=input(question)

if colorinput == alien_color:
    print(">>>>\tYou have earned 5 points.")
else:
    exit()

