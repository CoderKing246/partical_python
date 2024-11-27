# Program to perform prime number operations: Check if a number is prime, generate primes up to a number, and generate the first N primes.

def is_prime(num):
    """
    Check if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_till_n(n):
    """
    Generate all prime numbers up to 'n'.
    """
    return [i for i in range(2, n + 1) if is_prime(i)]

def first_n_primes(n):
    """
    Generate the first 'n' prime numbers.
    """
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

    

def main():
    """
    Main function to drive the program.
    """
    while True:
        """
        Display menu options to the user.
        """
        print("\nMenu:")
        print("1. Check if a number is prime")
        print("2. Generate all prime numbers up to a given number")
        print("3. Generate the first N prime numbers")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Check if a number is prime
                n = int(input("Enter a number to check if it is prime: "))
                if is_prime(n):
                    print(f"{n} is a prime number.")
                else:
                    print(f"{n} is not a prime number.")
            elif choice == 2:
                # Generate all prime numbers up to a number
                n = int(input("Enter a number to generate all primes up to it: "))
                if n < 0:
                    print("Please enter a non-negative number.")
                else:
                    primes_up_to_n = primes_till_n(n)
                    print(f"All prime numbers up to {n}: {primes_up_to_n}")
            elif choice == 3:
                # Generate the first N prime numbers
                n = int(input("Enter how many prime numbers to generate: "))
                if n <= 0:
                    print("Please enter a positive number.")
                else:
                    first_primes = first_n_primes(n)
                    print(f"The first {n} prime numbers are: {first_primes}")
            elif choice == 4:
                # Exit the program
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Entry point of the program
if __name__ == "__main__":
    main()