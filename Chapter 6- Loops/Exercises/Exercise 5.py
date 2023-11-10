# No Pastrami

## Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
## Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
## Make sure no pastrami sandwiches end up in finished_sandwiches.


##### Attempt

sandwich_orders=['Ham and cheese', 'Pastrami', 'Chicken mayo', 'Salmon and cream cheese', 'Pastrami', 'Cheese and tomato', 'BLT', 'Pastrami']
finished_sandwiches=[]

print("We ran out of Pastrami!")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print('\n')
while sandwich_orders:
    wip=sandwich_orders.pop()
    print(f"We're working on your {wip} sandwich!")
    finished_sandwiches.append(wip)

print('\n')
for order in finished_sandwiches:
    print(f"Order up! The {order} sandwich is ready.") 




