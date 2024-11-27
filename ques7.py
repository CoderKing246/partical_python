def find_occurrences(str1, str2):
    """
    Function to find all occurrences of str2 in str1 and return their starting indices.
    If str2 is not found in str1, returns -1.
    """
    # List to store the starting indices of occurrences
    indices = []
    
    # Find all occurrences of str2 in str1
    index = str1.find(str2)
    while index != -1:
        indices.append(index)
        index = str1.find(str2, index + 1)  # Continue searching from the next position
    
    # If no occurrences found, return -1
    if len(indices) == 0:
        return -1
    
    return indices

def main():
    # Input two strings
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string to find in the first string: ")

    # Find and print the occurrences of str2 in str1
    result = find_occurrences(str1, str2)
    
    if result == -1:
        print(f"The string '{str2}' is not found in '{str1}'.")
    else:
        print(f"The occurrences of '{str2}' in '{str1}' are at indices: {result}")

# Call the main function
main()
