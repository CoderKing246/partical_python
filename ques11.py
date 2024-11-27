'''
Write a function that prints a dictionary where the keys are numbers between 1 and 5
and the values are cubes of the keys
'''

def print_cubes_dict():
    try:
        # Generate the dictionary with keys as numbers and values as their cubes
        cubes_dict = {i: i ** 3 for i in range(1, 6)}
        print("Dictionary of cubes:", cubes_dict)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Call the function
print_cubes_dict()


