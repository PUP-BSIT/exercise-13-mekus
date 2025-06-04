import os
import modules

CHOICES = (0, 1, 2, 3, 4, 5)

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the main menu for the Mekus modules."""
    clear_screen()  # Clear the screen before showing the menu
    print(
        "\n === Mekus Module Menu ==="
        "\n [1] Agulto's Module"
        "\n [2] Dazo's Module"
        "\n [3] Jundam's Module"
        "\n [4] Olazo's Module"
        "\n [5] Serohijo's Module"
        "\n [0] Exit"
    )

def get_user_choice():
    """Get the user's choice from the menu."""
    # Ask the user to enter their menu choice
    user_input = input("Enter your choice: ")

    # Check if the input is composed only of digits
    if user_input.isdigit():
        # Convert the input string to an integer
        choice = int(user_input)

        # Check if the choice is in the list of valid options (CHOICES)
        if choice in CHOICES:
            return choice  # Return the valid choice

        # If the number is not in the list of valid options, show an error
        print("Invalid choice. Please try again.\n")
        return None

    # If the input is not a number, show an error
    print("Invalid input. Please enter a number.\n")
    return None  # Return None to indicate invalid input

def handle_user_choice(choice):
    """Handles the user's choice and calls the corresponding module."""
    match choice:
        case 1:
            # Call Agulto's module
            modules.agulto_main()
        case 2:
            # TODO: Implement Dazo's module
            pass
        case 3:
            # Call Jundam's module
            modules.jundam_main()
        case 4:
            # Call Olazo's module
            modules.olazo_main()
        case 5:
            # TODO: Implement Serohijo's module
            pass

def main():
    """Main function to run the Mekus modules."""
    while True:
        # Display the menu and get user choice
        display_menu()

        # Get the user's choice
        choice = get_user_choice()

        # If the choice is 0, exit the program
        if choice == 0:
            print("Exiting the program. Goodbye!")
            break

        # Handle the user's choice
        handle_user_choice(choice)

        # Wait before returning
        input("\nPress Enter to return to the main menu...")

main()