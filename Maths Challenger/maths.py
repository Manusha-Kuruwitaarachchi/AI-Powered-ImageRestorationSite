import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10    # why i use capital letter to show them are constants which means that will not change


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) #eval function unable us to evaluate the answer with using if to say if the operation is add  
    return expr, answer

wrong = 0
correct_first_attempt = 0
correct_after_attempts = 0

input("Press enter to start! ")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    attempts = 0
    
    while attempts < 2:
        guess = input(f"Problem #{i + 1}: {expr} = ")
        
        if guess.lower() == 'e':
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print("---------------------")
            print("Game stopped by user.")
            print("You finished the game in", total_time, "seconds!")
            print("You got", correct_first_attempt, "correct answer(s) on the first attempt.")
            print("You got", correct_after_attempts, "correct answer(s) after attempts.")
            print("You got", wrong, "wrong answer(s).")
            exit()
        
        if guess == str(answer):
            if attempts == 0:
                correct_first_attempt += 1
            else:
                correct_after_attempts += 1
                wrong -= 1  # Deduct from wrong as it's corrected in the second attempt
            break
        
        attempts += 1
        wrong += 1
        if attempts == 2:
            print(f"Incorrect. The correct answer was {answer}. Moving to the next problem.")
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------")
print("Nice Work! You finished the game in", total_time, "seconds!")
print("You got", correct_first_attempt, "correct answer(s) on the first attempt.")
print("You got", correct_after_attempts, "correct answer(s) after attempts.")
print("You got", wrong, "wrong answer(s).")
