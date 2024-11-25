# WAP to find the roots of a quadratic equation
import math
def roots(a,b,c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant>0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    
    elif discriminant == 0:
        root1 = (-b)/2*a*c
        return root1,root1
    else:
        # Complex roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return complex(root1.real, root1.imag), complex(root2.real, root2.imag)
    
print('ax2 + bx + c = 0')
a = int(input('Enter the value of a : '))
b = int(input('Enter the value of b : '))
c = int(input('Enter the value of c : '))

roots_values = roots(a, b, c)
print(f'The Roots of {a}x2 + {b}x + {c} are {roots_values}')