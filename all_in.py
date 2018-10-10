import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

inputs = sys.argv[1]
inputs=inputs.split(",")

def City_State(value):
    key=None
    for letter, city in capital_cities.items():
        if city.lower() == value.lower():
            key=(letter,city, 'City')

    for state, letter in states.items():
        if state.lower() == value.lower():
            key=(letter,state, 'State')
    return (key)

def phrase(key,name):
    if key==None:
        phr=name + ' is neither a capital city nor a state' 
    else:
        if key[2]=='City':
            for state, letter in states.items():
                if letter == key[0]:
                    phr=key[1] + " is the capital of " + state
        if key[2]=='State':
            for letter, city in capital_cities.items():
                if letter == key[0]:
                    phr=city + " is the capital of " + key[1]
    return phr

for element in inputs:
    element=element.lstrip()
    if element!='':
        key=City_State(element)
        print(phrase(key,element))

            
