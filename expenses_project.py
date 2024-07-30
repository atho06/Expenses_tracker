import json
import os

def file():
    print("""MENU
1.Load an existing user
2.Create user""")
    ch=int(input("Enter your choice:"))
    return ch

def select_user():
    for i in os.listdir('homeworkpyth'):##proper file name
        print(i)
    name=input("Enter user:")
    if name+'.py'.lower() in os.listdir('homeworkpyth'):##proper file name
        return name
    else:
        print("User not found!!!") 

def menu():#name function properly!!!
    print("""MENU:
1. Add expenses
2.Display statistics
""")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("""1. Food
2. Transportation
3. Education
4. Entertainment
5. Clothing
6. Health care
7. Housing
8.Enter new category""")
        ch=int(input("Enter your choice:"))
        if ch==8:
            expense={}
            ex_kind=input("Kind of expense:")
            amt=float(input("Enter expense:"))
            expense[ex_kind]=amt
        elif ch==1:
            print("asdfghjkl")
        elif ch==2:
            print("zcvbnm,")
        else:
            print("12345678")
        


#MAIN
print("""***********************
*  EXPENSE TRACKER  *
***********************""")
if file()==1:
    name=select_user()+'.json'
    print("--------",name,"--------")
    menu()
    #file=open(name, 'r')   #guessing file's datatype is dictionary
    #file.update(new_data)    new_data is also a dictionary
    print(name)





















    
