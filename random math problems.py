import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 15
TOTAL_PROBLEMS = 3 #can be increased as per choice

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press Enter to start!")
print(">>>>>>>>>>>>>>>>>>>")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem # {i+1}: {expr} = ")
        if guess == str(answer):
            break  # Correct answer: exit the loop
        wrong += 1  # Only increment if the answer is wrong

end_time = time.time()
total_time = end_time - start_time

print(">>>>>>>>>>>>>>>>>>")
print("Great job!")
print(f"Time taken: {round(total_time, 2)} seconds!")
print(f"Wrong attempts: {wrong}")