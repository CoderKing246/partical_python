'''
Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to perform following operations:
a. Print half the values of the tuple in one line and the other half in the next line.
b. Print another tuple whose values are even numbers in the given tuple.
c. Concatenate a tuple t2=(11,13,15) with t1.
d. Return maximum and minimum value from this tuple
'''

# Given tuple
t1 = eval(input('Enter the Tuple : '))

try:
    # a. Print half the values of the tuple in one line and the other half in the next line
    mid = len(t1) // 2
    print("First half:", t1[:mid])
    print("Second half:", t1[mid:])

    # b. Print another tuple whose values are even numbers in the given tuple
    even_numbers = tuple(x for x in t1 if x % 2 == 0)
    print("Even numbers tuple:", even_numbers)

    # c. Concatenate a tuple t2=(11,13,15) with t1
    t2 = (11, 13, 15)
    concatenated_tuple = t1 + t2
    print("Concatenated tuple:", concatenated_tuple)

    # d. Return maximum and minimum value from this tuple
    print("Maximum value:", max(t1))
    print("Minimum value:", min(t1))

except Exception as e:
    # Handle any unexpected errors
    print(f"An error occurred: {e}")

