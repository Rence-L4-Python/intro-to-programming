# Glossary 2

## Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
## When you’re sure that your loop works, add five more Python terms to your glossary.
## When you run your program again, these new words and meanings should automatically be included in the output.


##### Attempt

print("[Glossary]\n")

glossary={
'string':"a sequence of characters which can contain letters, numbers, symbols, and spaces.",
'else':"a conditional statement that executes if the 'if' statement resolves to a false value.",
'if':"a conditional statement that executes a condition if it is true.",
'print':"a function that prints a message to the a screen",
'dictionary':"a collection of a key-value pairs.",
'loop':"a control flow statement used to repeatedly execute a group of statements when conditions are true",
'list':"a class of data structure used to store multiple items in one variable",
'variable':"a container for storing data values",
'comment':"lines of code ignored by the Python interpreter",
'import':"allows modules to be imported into code ",
}

## keys:values
for word, description in glossary.items():
    print(f"\n{word.title()}: \n>  {description}")