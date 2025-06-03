import os

CHOICES = (0, 1, 2, 3)

def display_menu():
    """ Display the main menu """
    print(
        "=== === Get to know Jermaine === ===\n"
        "[1] Basic Info\n"
        "[2] Goals\n"
        "[3] Dazo - Comment\n"
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
    """ Display Jermaine's basic information """
    print(
        "Basic Information:\n"
        "\tName: Jermaine Razehl Agulto\n"
        "\tAge: 20\n"
        "\tHobbies: Travel, Playing sports, Coding, Gaming\n"
    )

def display_goals():
    """ Display Jermaine's goals """
    print(
        "Goals:\n"
        "\t1. Try a new sport or challenge\n"
        "\t2. Build a strong professional network\n"
        "\t3. Start a business or side hustle\n"
    )

def handle_user_choice(choice):
    """ Handle the user's choice from the menu """
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            print("Coding and Playing at the same time? Nice! \n")

def agulto_main():
    """ Main function to run the program """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Exiting the program. Goodbye!\n")
            break

        handle_user_choice(choice)

        input("Press Enter to continue...")

agulto_main()