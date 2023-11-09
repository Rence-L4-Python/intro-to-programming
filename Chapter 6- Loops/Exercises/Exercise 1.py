# Pizza Toppings

## Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
## As they enter each topping, print a message saying you’ll add that topping to their pizza.


##### Attempt
## Pizza Toppings Tool
ask = "\nWhat topping would you like on your pizza?"
ask += "\nPlease type 'quit' when you have nothing else to add: "

## Please type the toppings as-is, they are case sensitive!
available_toppings=["bbq chicken", "black olives", "cheese", "garlic", "herb", "mushroom", "pepperoni", "tomato sauce"]

while True:
    print("\n===============", "\nAVAILABLE PIZZA TOPPINGS:", "\n", "bbq chicken, black olives, cheese, garlic, herb, mushroom, pepperoni, tomato sauce", "\n===============")
    pizza_toppings=input(ask)
    if pizza_toppings == 'quit':
        exit()
    elif pizza_toppings not in available_toppings:
        print(">>>>\t[Sorry! That topping is not available.]")
    else:
        print(f">>>>\t[I'll be adding {pizza_toppings} to your pizza!]\n")
       
