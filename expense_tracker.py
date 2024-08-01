import json

def create_user():
    with open('user.json', 'w') as file:
        expenses = {'Food': 0, 'Transportation': 0, 'Entertainment': 0, 'Education': 0, 'Clothing': 0, 'Housing': 0}
        json.dump(expenses, file)

def load_user():
    try:
        with open('user.json', 'r') as file:
            expenses = json.load(file)
            print("User loaded successfully.")
            return expenses
    except FileNotFoundError:
        print("File not present!!!")
        create_user()
        with open('user.json', 'r') as file:
            expenses = json.load(file)
            print("User loaded successfully.")
            return expenses


def display(expenses):
    total_amt = sum(expenses.values())
    if total_amt == 0:
        print("No expenses")
        return
    for key, value in expenses.items():
        val = (value / total_amt) * 10
        print("|||" * int(val), "-------------->", key)

def menu(expenses):
    menu = ['Food', 'Transportation', 'Entertainment', 'Education', 'Clothing', 'Housing']
    while True:
        print("""\n\nMENU:
1. Add expenses
2. Display statistics
3. EXIT
""")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            for i in range(len(menu)):
                print(i + 1, ".", menu[i])
            ch = int(input("Enter your choice: "))
            if ch <= len(menu):
                cat = menu[ch - 1]
                add_amt = float(input("Enter amount to be added: "))
                expenses[cat] += add_amt
            else:
                print("Enter valid choice!!!")
        elif ch == 2:
            display(expenses)
        elif ch == 3:
            with open('user.json', 'w') as file:
                json.dump(expenses, file)
            break
        else:
            print("Enter valid option!!!")

# MAIN
print("""***********************
*  EXPENSE TRACKER  *
***********************""")

expenses = load_user()
menu(expenses)
