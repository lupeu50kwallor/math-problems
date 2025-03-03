
import random

def get_random_math_problem(max_value=100):
    operands = [random.randint(1, max_value), random.randint(1, max_value)]
    operator = random.choice(["+", "-", "*", "/"])
    solution = eval(f"{operands[0]} {operator} {operands[1]}")
    return f"What is {operands[0]} {operator} {operands[1]}?\nAnswer: {solution}"