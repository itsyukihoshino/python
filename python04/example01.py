import random                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                           
user_wins = 0
computer_wins = 0

options =  ["rock","paper","scissor"]                                                                                                                                                                                                                                                                                                                                        


while True:
     user_input = input("Type rock/paper/scissors or Q to quit:").lower()
    if user_input == "q":
        break
    if user input not in options:
        continue

random_number = random.randint(0, 2)
# rock: 0, paper: 1, scissors: 2
computer_pick = options[random_number]















