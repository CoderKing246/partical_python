def cubes_of_even_integers_for_loop(input_list):
    """
    Function to create a list of cubes of even integers using a 'for' loop.
    """
    result = []
    for item in input_list:
        if isinstance(item, int) and item % 2 == 0:
            result.append(item ** 3)
    return result

def cubes_of_even_integers_comprehension(input_list):
    """
    Function to create a list of cubes of even integers using list comprehension.
    """
    return [item ** 3 for item in input_list if isinstance(item, int) and item % 2 == 0]

def main():
    # Sample input list that may contain integers, strings, and other types
    input_list = [2, 5, 8, 'hello', 12, 7.5, 4, 'world', 6]
    
    # Using 'for' loop
    result_for_loop = cubes_of_even_integers_for_loop(input_list)
    print("Cubes of even integers using 'for' loop:", result_for_loop)
    
    # Using list comprehension
    result_comprehension = cubes_of_even_integers_comprehension(input_list)
    print("Cubes of even integers using list comprehension:", result_comprehension)

# Call the main function
main()