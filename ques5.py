def find_frequency(s, char):
    """
    Function to find the frequency of a character in the string.
    """
    return s.count(char)

def replace_character(s, old_char, new_char):
    """
    Function to replace a character by another character in the string.
    """
    return s.replace(old_char, new_char)

def remove_first_occurrence(s, char):
    """
    Function to remove the first occurrence of a character from the string.
    """
    return s.replace(char, '', 1)

def remove_all_occurrences(s, char):
    """
    Function to remove all occurrences of a character from the string.
    """
    return s.replace(char, '')

def main():
    # Take user input for string and character
    s = input("Enter a string: ")
    char = input("Enter a character to perform operations on: ")

    print("\nChoose the operation you want to perform:")
    print("1. Find the frequency of a character in the string")
    print("2. Replace a character by another character in the string")
    print("3. Remove the first occurrence of a character from the string")
    print("4. Remove all occurrences of a character from the string")
    
    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        
        if choice == 1:
            frequency = find_frequency(s, char)
            print(f"The frequency of character '{char}' in the string is: {frequency}")
        
        elif choice == 2:
            new_char = input(f"Enter the new character to replace '{char}': ")
            modified_string = replace_character(s, char, new_char)
            print(f"The modified string is: {modified_string}")
        
        elif choice == 3:
            modified_string = remove_first_occurrence(s, char)
            print(f"The string after removing the first occurrence of '{char}': {modified_string}")
        
        elif choice == 4:
            modified_string = remove_all_occurrences(s, char)
            print(f"The string after removing all occurrences of '{char}': {modified_string}")
        
        else:
            print("Invalid choice! Please enter a valid option (1/2/3/4).")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Call the main function
main()
