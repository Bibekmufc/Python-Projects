
from art import logo


#Add function

def add(n1, n2):
    return n1 + n2

#Subtract function
def subtract(n1, n2):
    return n1 - n2

#Multiply function
def multiply(n1, n2):
    return n1 * n2

#Divide function
def divide(n1, n2):
    return n1 / n2


#list of operators
operation = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide}


#Calculator function where everything happens
def calculator():
    print(logo)
    num1 = float(input(f"What's the first number?: ")) #input for first number
    for symbol in operation:
        print(symbol)
    should_continue = True

    #a while loop that tells to keep the program running
    while should_continue:
        operation_symbol = input(f"Pick an operation symbol: ") #input for the operation
        if not operation_symbol in(["+", "-", "*", "/"]): #if statement to check for valid symbol
            print("Please type a valid operator")
            continue
        num2 = float(input(f"What's the next number?: ")) #input for the second number
        calculation = operation[operation_symbol] #calling the operation dictionary for it's value
        answer = calculation(num1, num2) #assigning the result to answer variable

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        resume = input(f"Type 'y' to to continue calculating with {answer}, or type 'n' to start over, or any other key to exit: ") #input to restart, start over, or close 

        #if statement to check the input
        if not(resume in ['y', 'n']):
            exit()
        elif resume == 'y':
            num1 = answer
        elif resume == 'n':
            should_continue = False
            calculator()        #recursing the calculator function to start the program again

calculator() #calling the function to start the program