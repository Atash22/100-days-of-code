from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculate():
    number1 = int(input("Type a number\n"))
    while True:
        operator = (input("Type an operator: \n+, -, *, /, \n"))
        number2 = int(input("Type another number\n"))
        result = operations[operator](number1, number2)
        print(f"Calculation result is {result}")

        continue_result = input("Do you want to continue with the previous result? yes or no or finish?\n")
        if continue_result == "yes":
            number1 = result
        elif continue_result == "no":
            calculate()
        else:
            break

calculate()