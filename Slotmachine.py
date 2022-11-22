import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "d": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "d": 2
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, SYMBOL_COUNT in symbols.items():
        for _ in range(SYMBOL_COUNT):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
        print()


def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol !=symbol_to_check:
                break
        else:
            winnings +=values[symbol]*bet
            winnings_lines.append(lines+1)

    return winnings,winnings_lines


def deposit():
    while True:
        amount = input("What would you like to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater then 0")
        else:
            print("please enter a number ")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("lines  must be according to the constraint")
        else:
            print("please enter a number ")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("please enter a number ")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you do not have enough to bet,your current balance is ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to :${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won {winnings}.")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is {balance}")
        answer = input("press enter to spin (q to quit)")
        if answer == "q":
            break
        balance+=spin(balance);
    print(f"you left with {balance}")


main()
