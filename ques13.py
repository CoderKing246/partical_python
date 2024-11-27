'''
WAP to accept a name from a user. Raise and handle appropriate exception(s) if the
text entered by the user contains digits and/or special characters.
'''
class InvalidNameError(Exception):
    """Custom exception for invalid name input."""
    pass

def accept_name():
    try:
        name = input("Enter your name: ")
        
        # Check if the name contains digits or special characters
        if not name.isalpha():
            raise InvalidNameError("Name must only contain alphabetic characters.")
        
        print(f"Hello, {name}!")
    
    except InvalidNameError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
accept_name()
