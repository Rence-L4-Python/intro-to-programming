# Cities

## Write a function called describe_city() that accepts the name of a city and its country. 
## The function should print a simple sentence, such as Reykjavik is in Iceland. 
## Give the parameter for the country a default value.
## Call your function for three different cities, at least one of which is not in the default country.


##### Attempt

print('Describing cities:\n')

def describe_city(city, country='Norway'):
    text = city + " is in " + country + "."
    print(text)

describe_city('Oslo')
describe_city('Warsaw', 'Poland') 
describe_city('Trondheim')   

