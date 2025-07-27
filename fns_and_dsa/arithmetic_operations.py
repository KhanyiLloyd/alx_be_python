def perform_operation(num1:float, num2:float, operation:str):
    """
    Function performs basic arithmetic operations.
    The first number is a float
    The second number is a float 
    The operation +,-,*,/ are strings
    Result returns a float or a string or an error message when dividing by zero
    
    """
    if operation == "add":
        return num1+num2
    elif operation == "subtract":
        return num1-num2
    elif operation == "multiply":
        return num1*num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero in not permissible"
        return num1/num2
    else:
        return "Error: Invalid operation."