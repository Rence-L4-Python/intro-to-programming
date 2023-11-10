# T-Shirt

## Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
## The function should print a sentence summarizing the size of the shirt and the message printed on it.
## Call the function once using positional arguments to make a shirt. 
## Call the function a second time using keyword arguments.


##### Attempt

print("Shirt printer:")

def make_shirt(size, text):
    print("\nThe machine will be printing a " + size + " shirt.")
    print('It will say the quote: "' + text + '"')

make_shirt('small', 'A year from now you may wish you had started today.')
make_shirt(size='large', text="It always seems impossible until it's done.")