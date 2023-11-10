# Glossary 1

## A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
### * Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
### * Print each word and its meaning as neatly formatted output. 
## You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line.
## Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.


##### Attempt

print("[Glossary]\n")

glossary={
'string':"a sequence of characters which can contain letters, numbers, symbols, and spaces.",
'else': "a conditional statement that executes if the 'if' statement resolves to a false value.",
'if': "a conditional statement that executes a condition if it is true.",
'print': "a function that prints a message to the a screen",
'dictionary': "a collection of a key-value pairs.",
}

word = 'string'
print(f"{word.title()}: \n>  {glossary[word]}")
word = 'else'
print(f"{word.title()}: \n>  {glossary[word]}")
word = 'if'
print(f"{word.title()}: \n>  {glossary[word]}")
word = 'print'
print(f"{word.title()}: \n>  {glossary[word]}")
word = 'dictionary'
print(f"{word.title()}: \n>  {glossary[word]}")


###### Shortening code attempt

print("\n\n[Personal Activity]: Shortening code\n")
print("[Glossary]\n")

glossary={
'string':"a sequence of characters which can contain letters, numbers, symbols, and spaces.",
'else': "a conditional statement that executes if the 'if' statement resolves to a false value.",
'if': "a conditional statement that executes a condition if it is true.",
'print': "a function that prints a message to the a screen",
'dictionary': "a collection of a key-value pairs.",
}

for word, description in glossary.items():
    print(f'{word}: \n>  {description}')