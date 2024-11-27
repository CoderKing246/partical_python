def print_pyramid(n):
    """
    Function to print a pyramid of '*' with 'n' rows.
    """
    for i in range(1, n + 1):
        # Print spaces before stars
        print(' ' * (n - i) + '*' * (2 * i - 1))

def print_reverse_pyramid(n):
    """
    Function to print a reverse pyramid of '*' with 'n' rows.
    """
    for i in range(n - 1, 0, -1):
        # Print spaces before stars
        print(' ' * (n - i) + '*' * (2 * i - 1))

def main():
    n = 5  # Number of rows for the pyramid
    print("Pyramid:")
    print_pyramid(n)
    print("\nReverse Pyramid:")
    print_reverse_pyramid(n)

# Call the main function
main()
