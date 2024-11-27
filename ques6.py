def swap_first_n_chars(str1, str2, n):
    """
    Function to swap the first n characters of two strings.
    """
    if n > len(str1) or n > len(str2):
        print("Error: 'n' is greater than the length of one of the strings.")
        return str1, str2
    
    # Swap the first n characters
    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]
    
    return new_str1, new_str2

def main():
    # Input two strings
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    n = int(input("Enter the number of characters to swap: "))

    # Swap the first n characters and display the result
    swapped_str1, swapped_str2 = swap_first_n_chars(str1, str2, n)
    print(f"After swapping the first {n} characters:")
    print(f"New first string: {swapped_str1}")
    print(f"New second string: {swapped_str2}")

# Call the main function
main()
