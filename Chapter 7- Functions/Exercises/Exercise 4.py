# Large Shirts

## Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
## Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


##### Attempt

print("Shirt printer: default large size")

def make_shirt(size='large', text='I love Python.'):
    print("\nThe machine will be printing a " + size + " shirt.")
    print('It will say something like: "' + text + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('large', 'Technical artists rock!')