import math

def roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    
    elif discriminant == 0:
        # One real root (double root)
        root1 = -b / (2*a)
        return root1, root1
    
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Input quadratic equation coefficients
print('Quadratic Equation: ax^2 + bx + c = 0')
try:
    a = int(input('Enter the value of a: '))
    b = int(input('Enter the value of b: '))
    c = int(input('Enter the value of c: '))
    
    if a == 0:
        print("This is not a quadratic equation (a cannot be zero).")
    else:
        roots_values = roots(a, b, c)
        print(f'The roots of the equation {a}x^2 + {b}x + {c} = 0 are: {roots_values}')
except ValueError:
    print("Invalid input. Please enter numerical values.")
except Exception as e:
    print(f"An error occurred: {e}")