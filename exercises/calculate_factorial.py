# implement factorial_recursive method
def factorial_recursive(number):
    if number < 2:
         return 1
    return number * factorial_recursive(number - 1)

def factorial_iterative(number):
    if number < 2:
        return 1
    factorialResult = 1
    for i in range(1, number + 1):
        factorialResult *= i
    return factorialResult

def process_input(input_str):
    error_message = ''
    value = None
    # handle negative input
    try:
        value = int(input_str)
        if value < 0:
            return None, "Number cannot be negative"
    except ValueError as ex:
        error_message = "Number must be an integer"
        return value, error_message
    return value, error_message

def handle_recursive_limit(input_number):
   if input_number < 998:
       value = factorial_recursive(input_number)
   else:
       value = factorial_iterative(input_number)
   return value

def main():
    value = None
    print("Factorial Computation Using Recursion")
    while value is None:
        number = input("Enter a non-negative integer: ")
        value, error_message = process_input(number)

    # Call factorial_recursive method
    print("The factorial of", str(value), "is:", str(handle_recursive_limit(value)))

if __name__ == "__main__":
    main()
