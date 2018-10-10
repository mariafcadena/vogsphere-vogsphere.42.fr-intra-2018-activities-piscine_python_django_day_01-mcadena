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

input_state = sys.argv[1]

def State_Letter(search_state):
    for state, letters in states.items():
        if state == search_state:
            return(letters)

def Letter_City(search_letters):
    for letter, city in capital_cities.items():
        if letter == search_letters:
            return(city)

letter=State_Letter(input_state)
City=Letter_City(letter)
print(City)





