import random


def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        choice = random.randint(low, high)
        feedback = input(f"IF the {choice} is guess if high press 'H' if low press 'L' ")
        if feedback=='H':
            high = choice-1;
        elif feedback=='L':
            low = choice+1
    print("correct guess")

guess(10)