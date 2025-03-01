"""
this file contains core banking functions
"""
balance = 0.0

def deposit(amount: float) -> None:
    """Adds money to the user’s balance"""
    global balance
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number (int or float)")
    if amount <= 0:
        print("Deposit amount must be positive")
        return
    balance += float(amount)
    print(f"deposited {amount}")

def withdraw(amount: float) -> None:
    """Subtracts money from the user’s balance, checks for sufficient funds"""
    global balance
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number (int or float)")
    if amount <= 0:
        print("Withdrawal amount must be positive")
        return
    if amount > balance:
        print("Insufficient funds")
        return 
    balance -= float(amount)
    print(f'Withdrawn {amount}') 

def check_balance():
    """Displays the current balance"""
    return balance