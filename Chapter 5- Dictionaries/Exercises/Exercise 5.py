# Pets

## Make several dictionaries, where each dictionary represents a different pet. 
## In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
## Next, loop through your list and as you do, print everything you know about each pet.


##### Attempt

pets=[]

pet={
    'Species':'Cat',
    'Pet name':'Destroyer',
    'Owner name':'Mortis',
    'Age':'2',
    'Weight':'7kg',
    'Breed':'Ragdoll',
}
pets.append(pet)

pet={
    'Species':'Dog',
    'Pet name':'Princess',
    'Owner name':'Brad',
    'Age':'4',
    'Weight':'23kg',
    'Breed':'American Pit Bull Terrier',
}
pets.append(pet)

pet={
    'Species':'Bird',
    'Pet name':'Birdie',
    'Owner name':'Bauer',
    'Age':'34',
    'Weight':'700g',
    'Breed':'Cockatoo',
}
pets.append(pet)

pet={
    'Species':'Reptile',
    'Pet name':'Skye',
    'Owner name':'Gravis',
    'Age':'17',
    'Weight':'79kg',
    'Breed':'Komodo Dragon',
}
pets.append(pet)

for pet in pets:
    print(f"\n==========\nThis is everything we know about {pet['Pet name']}.")
    for key, value in pet.items():
        print(f"{key} : {value}")