# Deli

## Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
## Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
## As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.


##### Attempt

print('[Activity]')
sandwich_orders=['Ham and cheese', 'Chicken mayo', 'Salmon and cream cheese', 'Cheese and tomato', 'BLT']
finished_sandwiches=[]

print('\n')
while sandwich_orders:
    wip = sandwich_orders.pop()
    print(f"We're working on your {wip} sandwich!")
    finished_sandwiches.append(wip)

print('\n')
for order in finished_sandwiches:
    print(f'Order up! {order} sandwich is ready.')
print('\n')


###### sandwich ordering tool that shows available sandwiches, finished sandwiches, fake orders, repeated orders, when out of stock, and uses the time module

print('[Personal Activity]: Timed sandwich ordering tool\n')

ask="\n\tInput the sandwiches ordered by the customer: "

sandwich_orders=['Ham and cheese', 'Chicken mayo', 'Salmon and cream cheese', 'Cheese and tomato', 'BLT']
finished_sandwiches=[]
import time

print('\n')
while True:
    print(f'Currently available sandwiches: {sandwich_orders}','\n===============')
    order=input(ask)
    if order in sandwich_orders:
        print(f"\nThe {order} sandwich is currently being worked on!")
        finished_sandwiches.append(order)
        sandwich_orders.remove(order)
        sub=order
        time.sleep(2)
        print(f'>> Order up! The {sub} sandwich is ready to be delivered.\n')
        print('===============','\nList of finished sandwiches:', finished_sandwiches)
    elif order in finished_sandwiches:
        print(">> That has already been ordered.",'\n===============')
    else:
        print(">> That is not a real order.",'\n\n===============')
        pass
    if sandwich_orders == []:
        print('===============\n',"\n\t[WE RAN OUT OF SANDWICHES!]\n")
        break

