CHOICES = (0, 1, 2, 3, 4)

def display_menu():
    """Displays the main menu for the serohijos modules."""
    print(
        "=== Good Day! I am Joshua Serohijos ===\n"
        "[1] My Basic Info\n"
        "[2] My Goals\n"
        "[3] Dazo - Comment\n"
        "[4] Jundam - Comment\n"
        "[0] Exit\n"
    )

def get_user_choice():
    """
    Prompts the user for a choice and returns it.
    Returns the choice as an integer if valid, otherwise None.
    """
    user_input = input("Enter your choice: ")
    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        input("Press Enter to try again...")
        return None

    choice = int(user_input)
    if choice in CHOICES:
        return choice

    print("Invalid choice! Please try again.")
    input("Press Enter to try again...")
    return None

def display_basic_info():
    """Displays Joshua Serohijos's basic info."""
    print(
        "========== My Basic Info ==========\n"
        "Hello! I’m Joshua Serohijos, 19, from Pasay City.\n"
        "I'm a BSIT student at PUP-Taguig, eager to learn IT.\n"
    )

def display_goals():
    """Displays Joshua Serohijos's goals."""
    print(
        "========== My Goals ==========\n"
        "My short-term goal is to improve my skills in Python and networking\n"
        "Long-term, I aim to become a network engineer\n"
    )

def handle_user_choice(choice):
    """Handles the user's choice and calls the corresponding function."""
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            print("Goodluck on your Python and networking boy!\n")
        case 4:
            print(
                "Whoa! Already 19? Sheeeesh!\n" 
                "Becoming a network engineer is a great choice.\n" 
                "Wishing you all the best!\n")

def serohijos_main():
    """Main function to run the program."""
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice is None:
            continue
        
        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        
        handle_user_choice(choice)
        
        input("\nPress Enter to return to menu...")

serohijos_main()