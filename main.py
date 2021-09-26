from art import logo

def add(n1, n2):
    """Returns the sum of n1 + n2"""
    return n1 + n2


def sub(n1, n2):
    """Subtracts n2 from n1 (n1 - n2)"""
    return n1 - n2


def mul(n1, n2):
    """Multiplies n1 and n2"""
    return n1 * n2

def div(n1, n2):
    """Divides n1 and n2 (n1 / n2)"""
    if n2 == 0:
        print("Error: cannot divide by zero")
        return
    else:
        return n1 / n2

def calculator():
    """Allows to calculate two numbers"""  
    proceed = True    
    num1 = float(input("Enter first number\n> "))
    for symbol in operations:
        print(symbol)
    function = input("Please select one operator: ")
    num2 = float(input("Enter second number\n> "))

    memory = operations[function](num1,num2)
    while proceed:
        print (f"{num1} {function} {num2} = {memory}")

        if input(f"Proceed with {memory} ? (y/n)\n> ").lower() == "n":
            proceed = False
            break
        else:
            proceed = True
        for symbol in operations:
            print(symbol)
        num1 = memory
        function = input("Please select operator: ")
        num2 = float(input(function + " what number?\n> "))
        memory = operations[function](num1,num2)

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,

}

calculate_on = True

print(logo)
print("Welcome to the printing machine")

while calculate_on:
    calculator()

    if input("Start new Calculation?\n(y/n) > "):
        calculate_on = False
print("Good Bye :)")