from bank import *

def main():
    while True:
        user = input("Enter 'd' to deposit, 'w' to withdraw, 'b' to check balance, or 'exit' to quit:")
        if user.strip().lower() == 'd':
            try:
                amount = float(input("Enter amount to deposit :"))
                deposit(amount = amount)
            except ValueError:
                print("Invalid input! Please enter a valid number") 
                continue
        elif user.strip().lower() == 'w':
            try:
                amount = float(input("Enter amount to withdraw :"))
                withdraw(amount = amount)
            except ValueError:
                print("Invalid input! Please enter a valid number") 
                continue
        elif user.strip().lower() == 'b':
            print(f'Current balance :{check_balance()}')
            continue
        elif user.strip().lower() == 'exit':
            print("Exiting... Goodbye!")
            break
        else:
            print("Please Enter d / w / b / exit in correct")
            continue
    
if __name__ == "__main__":
    main()