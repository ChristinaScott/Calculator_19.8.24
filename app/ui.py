def get_input():
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        return x, y, operation
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return None, None, None

def display_result(result):
    print("Result:", result)
