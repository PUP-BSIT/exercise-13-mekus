import os

CHOICES = (0, 1, 2, 3, 4, 5)

def display_menu():
    """Display the main menu"""
    print(
        "=== This is John Albert Olazo's ===\n"
        "[1] Basic Info\n"
        "[2] Goals\n"
        "[3] Dazo - Comment\n"
        "[4] Jundam - Comment\n"
        "[5] Serohijos - Comment\n"
        "[0] Exit\n"
    )

def get_user_choice():
    """Get the user's choice from the menu"""
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
    """Display Albert's basic information"""
    print(
        "Basic Information:\n"
        "\tName: John Albert Olazo\n"
        "\tAge: 20\n"
        "\tHobbies: Music, Drawing, Coding, Gaming\n"
    )

def display_goals():
    """Display Albert's goals"""
    print(
        "Goals:\n"
        "\t1. Graduate with a bachelor's degree in Information Technology\n"
        "\t2. Become a proficient software developer\n"
        "\t3. Help my family achieve financial stability\n"
    )

def handle_user_choice(choice):
    """Handle the user's choice from the menu"""
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            print("Music with coffee is the death of me!\n")
            print("May the odds be ever yours\n")
        case 4:
            print(
                "Wow! So you're going to be an IT graduate? That’s awesome!\n"
                "Helping your family is a meaningful act of love.\n")
        case 5:
            print(
                "becoming a proficient software developer? That's good!\n"
            )

def olazo_main():
    """Main function to run the program"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Exiting the program. Goodbye!\n")
            break

        handle_user_choice(choice)

        input("Press Enter to continue...")

olazo_main()