def character_type(c):
    """
    Function to determine whether the character is a letter, numeric digit, or special character.
    """
    if c.isalpha():
        print(f"The character '{c}' is a letter.")
        if c.isupper():
            print("It is an uppercase letter.")
        else:
            print("It is a lowercase letter.")
    elif c.isdigit():
        print(f"The character '{c}' is a numeric digit.")
        print(f"Its name is {digit_to_text(c)}.")
    else:
        print(f"The character '{c}' is a special character.")

def digit_to_text(digit):
    """
    Convert a numeric digit to its textual representation.
    """
    digit_map = {
        '0': "ZERO", '1': "ONE", '2': "TWO", '3': "THREE", '4': "FOUR",
        '5': "FIVE", '6': "SIX", '7': "SEVEN", '8': "EIGHT", '9': "NINE"
    }
    return digit_map.get(digit, "UNKNOWN")

def main():
    c = input("Enter a character: ")

    if len(c) == 1:  # Check if the input is a single character
        character_type(c)
    else:
        print("Please enter only a single character.")

# Call the main function
main()