def solve_math_problem(n):
    problem = get_random_math_problem()
    solution = problem.solve(n)
    return solution

def get_random_math_problem():
    problems = {
        'addition': lambda x, y: x + y,
        'subtraction': lambda x, y: x - y,
        'multiplication': lambda x, y: x * y,
        'division': lambda x, y: x / y if y != 0 else None
    }
    operation = random.choice(list(problems.keys()))
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return problems[operation](num1, num2)
