import random

def get_random_python_code():
    """Generate a random Python code"""
    # Define a list of operators
    operators = ["+", "-", "*", "/"]

    # Generate a random equation using the operators
    left = random.randint(1, 10)
    right = random.randint(1, 10)
    operator = random.choice(operators)
    equation = f"{left} {operator} {right}"

    # Define a list of variables
    variables = ["x", "y", "z"]

    # Generate a random variable and assign it to the solution of the equation
    variable = random.choice(variables)
    solution = eval(equation)
    assignment = f"{variable} = {solution}"

    return assignment