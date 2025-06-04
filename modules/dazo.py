import os

CHOICES = (0, 1, 2, 3, 4, 5, 6)

def display_menu():
    """Displays the main menu for the Dazo modules."""
    print(
        "=== Good Day! I am Rollan Dazo :> ===\n"
        "[1] My Basic Info\n"
        "[2] My Goals\n"
        "[3] Jundam - Comment\n"
        "[4] Olazo - Comment\n"
        "[5] Serohijos - Comment\n"
        "[6] Agulto - Comment\n"
        "[0] Exit\n"
    )

def get_user_choice():
    """Prompts the user for a choice and returns it."""
    user_input = input("Enter your choice: ")

    if user_input.isdigit():
        choice = int(user_input)
        if choice in CHOICES:
            return choice

        print("Invalid choice. Please try again.\n")
        return None

    print("Invalid input. Please enter a number.\n")
    return None

def display_basic_info():
    """Displays Rollan Dazo's basic info."""
    print(
        "========== My Basic Info ==========\n"
        "Hello! I’m Rollan Dazo, 19, from Taguig City.\n"
        "I'm a 2nd year BSIT student at PUP-Taguig, eager to learn IT.\n"
        "I love exploring tech that solves real-world problems.\n"
        "I enjoy self-learning, coding, and time with friends and family.\n"
        "I value honesty, teamwork, and personal growth.\n"
    )

def display_goals():
    """Displays Rollan Dazo's goals."""
    print(
        "========== My Goals ==========\n"
        "My short-term goal is to improve my skills in Python\n"
        "and web development, and to join more coding projects.\n"
        "Long-term, I aim to become a software engineer or\n"
        "systems analyst who builds helpful, real-world apps.\n"
        "I also want to give back to my community through tech.\n"
    )

def handle_user_choice(choice):
    """Handles the user's choice and calls the corresponding function."""
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            print(
                "Software engineer? Dang, you must be talented!\n"
                "I believe you’ll make it!\n"
            )
        case 4:
            print(
                "Giving back to the community is a great goal!\n"
                "I’m sure you’ll achieve it!\n"
            )
        case 5:
            print(
                "Wow! 19 already? Time flies!\n"
                "I’m sure you’ll achieve your goals!\n"
            )
        case 6:
            print(
                "Nice! A 2nd year BSIT student already?\n"
                "Keep it up—you're on the right track!\n"
            )

def dazo_main():
    """Main function to run the program"""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        display_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Exiting the module. Goodbye!")
            break   

        handle_user_choice(choice)

        input("\nPress Enter to return to menu...")