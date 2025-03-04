import random

def get_random_math_problem(difficulty):
    if difficulty == "easy":
        numbers = [1, 2, 3, 4, 5]
    elif difficulty == "medium":
        numbers = [6, 7, 8, 9, 10]
    else:
        numbers = [11, 12, 13, 14, 15]
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    problem = f"What is {number1} x {number2}"
    solution = number1 * number2
    return problem, solution
