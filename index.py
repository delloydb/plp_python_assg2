def basic_calculator():
    print("Basic Calculator")
    try:
        # Getting user inputs
        num1 = float(input("Enter the first number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Performing the calculation based on the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return

        # Printing the result
        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Run the calculator
basic_calculator()
