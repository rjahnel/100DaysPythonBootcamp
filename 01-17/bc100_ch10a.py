# CALCULATOR
# 2.4.22 Rolf Jahnel
# in Corona Quarantäne :-(
#

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
    "/": divide,
}

def calculator():
    print("-======== C A L C U L A T O R ========-\n")
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    
    exit_loop = False
    while not exit_loop:   
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        operation = operations[op_symbol]
        result = operation(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {result}")
        cont = input(f"Type 'y' to continue calculating with {result}, or type 'r' to restart or 's' to stop: ")
        if cont == 'r':
            exit_loop = True
            calculator()
        elif cont == 'y': 
            num1 = result
        elif cont == 's':
            exit_loop = True
            print("=== End ===")
    
    
calculator()
