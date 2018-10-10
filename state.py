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

input_city = sys.argv[1]

def City_Letter(search_city):
    for letter, city in capital_cities.items():
        if city == search_city:
            return(letter)

def Letter_State(search_letter):
    for state, letters in states.items():
        if letters == search_letter:
            return(state)



letter=City_Letter(input_city)
State=Letter_State(letter)
print(State)





