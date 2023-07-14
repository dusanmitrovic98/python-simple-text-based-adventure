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
