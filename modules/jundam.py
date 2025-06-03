CHOICES = (0, 1, 2)

def display_menu():
    """ Displays the main menu """
    print(
        "=== Wazzup madlang pips, This is me Dann Kyle Jundam ===\n"
        "[1] Basic Info\n"
        "[2] Goals\n"
        "[0] Exit\n"
    )

def get_user_choice():
    """ Get the user's choice from the menu """
    user_input = input("Enter your choice: ")

    if user_input.isdigit():
        choice = int(user_input)
        if choice in CHOICES:
            return choice
        else:
            print("Invalid choice. Please try again.\n")
            return None

    print("Invalid input. Please enter a number.\n")
    return None

def display_basic_info():
    """ Display Kyle's basic information """
    print(
        "  === My Basic Info ===\n"
        "Name: Dann Kyle Jundam\n"
        "Age: 24 Years Old\n"
        "Birthday: April 3, 2001\n"
        "Hobbies: Watching action movies and riding motorcycle.\n"
    )

def display_goals():
    """ Display Kyle's goals """
    print(
        "  === My Goals ===\n"
        "- Graduate with a degree in IT\n"
        "- Get a stable job after graduation\n"
        "- Support and make my family proud\n"
        "- Keep improving my skills in tech\n"
    )

def handle_user_choice(choice):
    """ Handle the user's choice from the menu """
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()

def jundam_main():
    """ Main function to run the program """
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Exiting the program. Goodbye!\n")
            break

        handle_user_choice(choice)

        input("Press Enter to continue...\n")

jundam_main()