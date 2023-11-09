# Greetings

## Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. 
## The text of each message should be the same, but each message should be personalized with the person’s name.


##### Attempt
print('\nVersion 1: Personalized Message\n')
names=["Arthur", "John", "Charles"]

txt= f"Hey there, {names[0]}!"
print(txt)

txt= f"Hey there, {names[1]}!"
print(txt)

txt= f"Hey there, {names[2]}!"
print(txt)


### Test version, attempt to shorten code using 'for' loop
print('\n\n[Personal Activity]: Shortening code\n')
names=["Arthur", "John", "Charles"]
for txt in names:
    print(f"Mornin, {txt}! How's yer day goin' so far?")

exit()