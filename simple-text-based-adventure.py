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
