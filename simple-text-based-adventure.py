import time

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself standing in front of a mysterious door.")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)

def choose_door():
    print("1. Open the door")
    print("2. Knock on the door")
    print("3. Walk away")
    choice = input("Enter your choice: ")
    if choice == "1":
        open_door()
    elif choice == "2":
        knock_door()
    elif choice == "3":
        walk_away()
    else:
        invalid_choice()

def open_door():
    print("You open the door and find a magical world inside.")
    time.sleep(1)
    print("You see three paths ahead:")
    time.sleep(1)
    print("1. Follow the path to the enchanted forest.")
    print("2. Take the path leading to the ancient ruins.")
    print("3. Venture into the dark cave.")
    choice = input("Enter your choice: ")
    if choice == "1":
        enchanted_forest()
    elif choice == "2":
        ancient_ruins()
    elif choice == "3":
        dark_cave()
    else:
        invalid_choice()

def knock_door():
    print("You knock on the door and it swings open.")
    time.sleep(1)
    print("A friendly wizard welcomes you inside.")
    time.sleep(1)
    print("The wizard offers you a choice:")
    time.sleep(1)
    print("1. Learn powerful spells at the wizard's school.")
    print("2. Embark on a quest to save the kingdom.")
    choice = input("Enter your choice: ")
    if choice == "1":
        wizard_school()
    elif choice == "2":
        save_kingdom()
    else:
        invalid_choice()

def walk_away():
    print("You decide to walk away from the door.")
    time.sleep(1)
    print("As you walk, you stumble upon a hidden treasure.")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)
    print("1. Take the treasure and continue exploring.")
    print("2. Leave the treasure and keep walking.")
    choice = input("Enter your choice: ")
    if choice == "1":
        take_treasure()
    elif choice == "2":
        keep_walking()
    else:
        invalid_choice()

def keep_walking():
    print("You decide to leave the treasure behind and continue walking.")
    time.sleep(1)
    print("As you walk, you stumble upon a mysterious portal.")
    time.sleep(1)
    print("Curiosity gets the better of you, and you step into the portal.")
    time.sleep(1)
    print("You find yourself in a new dimension, filled with endless possibilities.")
    time.sleep(1)
    print("Congratulations! You have embarked on a new adventure.")
    time.sleep(1)
    play_again()

# Updated paths with fatal endings
def enchanted_forest():
    print("You enter the enchanted forest and encounter a mystical creature.")
    time.sleep(1)
    print("The creature grants you a powerful ancient artifact.")
    time.sleep(1)
    print("However, in your greed, you misuse its power and lose control.")
    time.sleep(1)
    fatal_ending()
def ancient_ruins():
    print("You arrive at the ancient ruins and discover a hidden chamber.")
    time.sleep(1)
    print("Inside the chamber, you find a legendary sword.")
    time.sleep(1)
    print("As you try to pull out the sword, a powerful curse is unleashed.")
    time.sleep(1)
    fatal_ending()

def dark_cave():
    print("You bravely enter the dark cave and hear a menacing growl.")
    time.sleep(1)
    print("You face a fearsome dragon and engage in an epic battle.")
    time.sleep(1)
    print("Despite your best efforts, the dragon overwhelms you with its power.")
    time.sleep(1)
    print("You are badly injured and unable to continue the fight.")
    time.sleep(1)
    print("As the dragon prepares for a final blow, you realize your fate.")
    time.sleep(1)
    print("With one last breath, you close your eyes and succumb to your injuries.")
    time.sleep(1)
    fatal_ending()

def wizard_school():
    print("You enroll at the wizard's school and begin your magical training.")
    time.sleep(1)
    print("Years later, you become a master wizard and teach at the school.")
    time.sleep(1)
    print("You pass on your knowledge to future generations of wizards.")
    time.sleep(1)
    print("Congratulations! You have become a respected and influential figure.")
    time.sleep(1)
    play_again()

def save_kingdom():
    print("You embark on a perilous journey to save the kingdom from an evil sorcerer.")
    time.sleep(1)
    print("With unwavering determination, you confront the sorcerer and defeat him.")
    time.sleep(1)
    print("The kingdom rejoices and hails you as their savior.")
    time.sleep(1)
    print("Congratulations! You have brought peace and prosperity to the land.")
    time.sleep(1)
    play_again()

def take_treasure():
    print("You take the treasure and feel its magical aura.")
    time.sleep(1)
    print("The treasure bestows upon you immense wealth and prosperity.")
    time.sleep(1)
    print("You live a life of luxury and fulfill all your dreams.")
    time.sleep(1)
