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
    "D": 8
}
symbol_winnings = {
        "A":5,
        "B":4,
        "C":3,
        "D":2
    }

def get_slot_machine_roll(ROWS, COLS, symbol_count):
    list_symbols = []
    for symbol, symbol_amount in symbol_count.items():
        for _ in range(symbol_amount):
            list_symbols.append(symbol)

    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = list_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(columns[i][row], end=" | ")
            else:
                print(columns[i][row])
    

def deposit():
    # Gather input for number machines
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if (amount > 0):
                break
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_lines():
    while True:
        num_lines = input("How many lines would you like to bet on (1 - " + str(MAX_LINES) +")? ")
        if num_lines.isdigit():
            num_lines = int(num_lines)
            if 0 < num_lines <= MAX_LINES:
                break
            else:
                print("Must bet on 1-3 lines to play!")
        else:
            print("Please enter a number.")
    return num_lines

def get_bet_amount():
    while True:
        bet_amount = input("How much would you like to bet on each line? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet_amount

def place_bet(amount, lines):
    # slot_machine_roll[col][row]
    print(f"You are betting ${amount} on {lines} lines. Total bet is ${amount * lines}.")
    print("Spinning!!!")
    slot_machine_roll = get_slot_machine_roll(ROWS, COLS, symbol_count)
    print_slot_machine(slot_machine_roll)
    return slot_machine_roll

def calculate_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        first_symbol = columns[0][line]
        for col in range(len(columns)):
            if columns[col][line] != first_symbol:
                break
        else:
            winnings += symbol_winnings[first_symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines
    
def main():
    balance = deposit()
    def userBet():
        nonlocal balance
        bet_size = get_bet_amount()
        bet_line_amount = get_number_lines()
        total_bet = bet_size * bet_line_amount
        if balance >= total_bet:
            current_roll = place_bet(bet_size, bet_line_amount)
            winnings, winning_lines = calculate_winnings(current_roll, bet_line_amount, bet_size)
            print(f"You received {winnings}.", end=" ")
            if (winnings < total_bet):
                print("Better luck next time.")
            elif winnings > 2 * total_bet:
                print("BIG WIN! Great job!")
                print(f"You won on lines: ", *winning_lines)
            else:
                print("Congratulations.")
                print(f"You won on lines: ", *winning_lines)

            balance = balance + winnings - total_bet
        else:
            print(f"Insufficient funds for total bet size of ${total_bet}. Your current balance is ${balance}. Please lower number of lines and/or bet amount.")
    while True:
        print(f"Welcome back. Your current balance is ${balance}.")
        start = input("Press enter to play (q to quit): ")
        if start == "q" or balance == 0:
            break
        else:
            userBet()
    
    print(f"You left with ${balance}.")

if __name__=="__main__":
    main()