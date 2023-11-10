# Rivers

## Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
## * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
## * Use a loop to print the name of each river included in the dictionary.
## * Use a loop to print the name of each country included in the dictionary.


##### Attempt

print("Rivers, Sentences:\n")

major_rivers={
'Yangtze':'China',
'Vistula':'Poland',
'Nakdong':'South Korea',
}

for rivers, countries in major_rivers.items():
    print(f"The {rivers} river runs through {countries}.")

## keys:values
print("\nNames of each river in the dictionary:")
for rivers in major_rivers.keys():
    print(f'> {rivers}')

print("\nNames of each country in the dictionary:")
for countries in major_rivers.values():
    print(f'> {countries}')
