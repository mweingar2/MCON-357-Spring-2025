# implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 or number == 1:
         return 1
    return number * factorial_recursive(number - 1)

def main():
    print("Factorial Computation Using Recursion")
    number = int(input("Enter a non-negative integer: "))

    # handle negative input
    while number < 0:
        number = int(input("Enter a non-negative integer: "))

    # Call factorial_recursive method
    print("The factorial of " + str(number) + " is: " + str(factorial_recursive(number)))

if __name__ == "__main__":
    main()
