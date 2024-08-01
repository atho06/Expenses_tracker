import json
import os.path

def file():
    print("""MENU
1.Load an existing user
2.Create user""")
    ch=int(input("Enter your choice:"))
    return ch

def create_user():
    name=input("Enter name of the user:")
    with open('USERS/' + name + '.json', 'w') as file:
        expenses={'Food':0, 'Transportation':0, 'Entertainment':0, 'Education':0, 'Clothing':0, 'Housing':0}
        json.dump(expenses,file)
    return name

def select_user():
    for i in os.listdir('USERS'):
        print(i)
    name=input("Enter user:")
    if name+'.json'.lower() in os.listdir('USERS'):
        return name
    else:
        print("User not found!!!")
        while True:
            ch=input("Do you want to create a new user?(yes/no):")
            if ch.lower()=='yes':
                return create_user()#returns name of user
            elif ch.lower()=='no':
                return None
            else:
                print("Enter valid answer!!!")

def display(name):
    if os.path.getsize('USERS/'+name) == 0:
        print("No expenses")
        return
    with open('USERS/'+name, 'r') as file:
        expenses=json.load(file)
        total_amt=sum(expenses.values())
        if total_amt==0:
            print("No expenses")
            return
        for key, value in expenses.items():
            val=(value/total_amt)*10
            print("|||"*int(val), "-------------->", key)

    
def menu():
    global name
    menu=['Food', 'Transportation', 'Entertainment', 'Education', 'Clothing', 'Housing', 'Add new category']
    while True:
        print("""\n\nMENU:
1. Add expenses
2.Display statistics
3.EXIT
""")
        ch=int(input("Enter your choice:"))
        if ch==1:
            for i in range (len(menu)):
                print(i+1, ".", menu[i])
            ch=int(input("Enter your choice:"))
            if ch==(len(menu)):
                new_category={}
                cat_kind=input("Kind of expense:")
                menu.insert((len(menu)-1), cat_kind) #adds to menu
                new_category[cat_kind]=None
                if os.path.getsize('USERS/'+name) == 0:
                    print("No expenses")
                    return
                with open('USERS/'+name, 'r') as file:
                    expenses = json.load(file)
                    expenses.update(new_category)
                with open('USERS/'+name, 'w') as file:
                    json.dump(expenses)
            elif ch<=len(menu):
                cat=menu[ch-1]
                add_amt=float(input("Enter amount to be added:"))
                if os.path.getsize('USERS/'+name) == 0:
                    print("No expenses")
                    return
                with open('USERS/'+name, 'r') as file:
                    expenses = json.load(file)
                amt=expenses[cat]
                amt+=add_amt
                expenses[cat]=amt
                with open('USERS/'+name, 'w') as file:
                    json.dump(expenses, file)
            else:
                print("Enter valid choice!!!")
        elif ch==2:
            display(name)
        elif ch==3:
            break
        else:
            print("Enter valid option!!!")



#MAIN
print("""***********************
*  EXPENSE TRACKER  *
***********************""")
while True:
    choice=file()
    if choice==1:
        name=select_user()
        if name:
            name+='.json'
            print("--------",name,"--------")
            menu()
            break
    elif choice==2:
        create_user()
    else:
        print("Enter valid option!!!")












