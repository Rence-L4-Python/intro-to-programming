# Movie Tickets

## A movie theater charges different ticket prices depending on a person’s age. 
## If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
## Write a loop in which you ask users their age, and then tell them the cost of their movie ticket


##### Attempt

ask=("Welcome to the Place-That-Will-Give-You-Discounts Movie Theater!")
ask+=("\nHow old are you?: ")

while True:
    print('\n===============\n', "[Your tickets will get a discount depending on your age]\n", "3 UNDER = FREE\n", "3 TO 12 = $10\n", "13 OVER = $15\n", '===============\n')
    age=int(input(ask))
    if age <3:
        print(">>>> Your ticket is free!")
    if age in range(3,13):
        print(">>>> Your ticket costs $10!")
    if age >12:
        print(">>>> Your ticket costs $15!")