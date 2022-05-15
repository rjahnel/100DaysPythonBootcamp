#Calculator

#Add
def add(n1, n2):
  '''Adds two numbers and returns their sum'''
  return n1 + n2

#Subtract
def subtract(n1, n2):
  '''Subtracts two numbers and returns their difference'''
  return n1 - n2

#Multiply
def multiply(n1, n2):
  '''Multyply two numbers and returns their product'''
  return n1 * n2

#Divide
def divide(n1, n2):
  '''Divide two numbers and returns their result'''
  return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
  num1 = float(input("What's your first number: "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  while should_continue:
    operation = input("Pick an operation? ")
    num2 = float(input("What's the next number: "))
    calculation = operations[operation]
    answer = calculation(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    
    if input("Keep on calc (yes/no)? ").lower() == "yes":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
