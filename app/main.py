import operations
import ui

def main():
    x, y, operation = ui.get_input()

    if operation == "+":
        result = operations.addition.add(x, y)
    elif operation == "-":
        result = operations.subtraction.subtract(x, y)
    elif operation == "*":
        result = operations.multiplication.multiply(x, y)
    elif operation == "/":
        result = operations.division.divide(x, y)
    else:
        result = "Invalid operation"

    ui.display_result(result)

if __name__ == "__main__":
    main()
