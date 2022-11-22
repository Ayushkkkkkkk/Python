import random


def choose(x):
    count = 0
    guesses = 0
    random_num = random.randint(1, x)
    while guesses != random_num:
        guesses = int(input(f"Enter the number between 1 to {x} and guess for the correct answer"))
        if guesses < random_num:
            print("enter a number greater then this")
            count += 1
        elif guesses > random_num:
            print("Enter a number lesser then this")
            count += 1
    count+=1
    print(f"you have guessed the correct number {random_num} in this {count} many guesses")

choose(10)
