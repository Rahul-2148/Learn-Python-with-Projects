# 1- import the random module from the random library of python 
import random

# 2- create subjects, actions and places
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Narendra Modi",
    "Auto Rikshaw Driver from Delhi",
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament house",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate",
]

# 3- start the Headline Generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    
    if user_input == "yes":
        continue
    
    if user_input == "no":
        break

# print a goodbye message
print("\nThanks for using the Fake Headline Generator. Have a fun day!")